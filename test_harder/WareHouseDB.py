import multiprocessing
import os
import sys
import time
import traceback
from datetime import datetime

import psycopg2
import pyodbc
from aimetricslib import CloudWatchMetrics
from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext
from openpyxl import Workbook

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory
parent_dir = os.path.dirname(current_dir)

# Add the parent directory to the Python path
sys.path.append(parent_dir)
import no_secret_config  # noqa: F401, E402
from logger import LoggerRegistry  # noqa: E402

_logger = None
WAREHOUSE_EXCEL_METRIC_NAMESPACE = "Automation.WarehouseExcel"

#######################
# QUERIES
#######################

SKU_SQL = """
SELECT
    SUM(quantity) AS qty,
    sku,
    timespan
FROM (
    SELECT
        items.quantity,
        items.id,
        items.sku AS sku,
        MAX(timestamp::date) AS timespan
    FROM orderitems items
    INNER JOIN orderitemlogs log ON items.id = log.orderitemid
    LEFT JOIN materialtypes mat ON items.materialtypeid = mat.id
    INNER JOIN orders orders ON orders.id = items.orderid
    WHERE
        action = 'SHIPPED'
        AND timestamp >= (CURRENT_TIMESTAMP - INTERVAL '1 day')
        AND timestamp <= CURRENT_TIMESTAMP
    GROUP BY 1, 2, 3
    ) AS asd
GROUP BY sku, timespan;
"""

RECIEVED_MATERIAL = """
SELECT
    dw.data,
    t.kodpaskowy AS barcode,
    t.kod AS kod,
    w.CDim_Parametr_FSC_Val AS FSC,
    dw.ilosc,
    t.jm AS unit,
    kh.Shortcut AS supplier,
    dw.ilosc * dw.cena AS value
FROM HM.DW AS dw
    LEFT JOIN SSCommon.HMF_WarehouseDeliveryClassification AS w ON w.ElementId = dw.id
    LEFT JOIN HM.tw AS t ON t.id = dw.idtw
    LEFT JOIN HM.ContractorsViewWithoutGUK AS kh ON kh.Id = dw.idkh
    LEFT JOIN HM.mz AS mz ON mz.id = dw.iddkzk
WHERE
    dw.data >= DATEADD(HOUR, -24, GETDATE())
    AND dw.data <= GETDATE()
    --AND dw.ilosc <> 0
    --AND dw.idkh > 0;
"""

FRAMES_SQL = """
WITH datasource AS (
    SELECT
        oi.quantity AS qty,
        oi.sku AS sku,
        CASE WHEN of.name IS NULL THEN 'UNKNOWN' ELSE of.name END AS frame_name,
        CONCAT(SUBSTRING(oi.sku FROM 7 FOR 3), 'x', SUBSTRING(oi.sku FROM 4 FOR 3)) AS size
    FROM orders o
    JOIN orderitems oi ON o.id = oi.orderid
    JOIN orderitemlogs oil ON oil.orderitemid = oi.id
    JOIN materialtypes mt ON oi.materialtypeid = mt.id
    LEFT JOIN orderitemframes of ON of.orderitemid = oi.id
    WHERE
        o.productionsiteid = 2
        AND mt.id = 2
        AND o.state = 'ARCHIVED'
        AND oil.action = 'SHIPPED'
        -- Last 24 hours
        AND oil.timestamp >= (CURRENT_TIMESTAMP - INTERVAL '1 day')
        AND oil.timestamp <= CURRENT_TIMESTAMP
    )
SELECT *
FROM datasource;
"""

#######################
# Logging & Metrics
#######################


def get_logger():
    """
    Lazy-initializes and returns the global logger.
    """
    global _logger
    if _logger is None:
        # TODO create logger in aws
        _logger = LoggerRegistry.get_logger("excel_db_queue", "excel_db_consumer")
    return _logger


def get_metrics():
    """
    Lazy-initializes and returns the CloudWatchMetrics client.
    """
    if not hasattr(get_metrics, "instance"):
        get_logger().info("Initializing CloudWatchMetrics client for ExcelDB process.")
        get_metrics.instance = CloudWatchMetrics(
            namespace=WAREHOUSE_EXCEL_METRIC_NAMESPACE,
            region="eu-central-1",
            logger=get_logger(),
        )
    return get_metrics.instance


#######################
# SharePoint Helper
#######################


def upload_excel_to_sharepoint(
    local_file_path, sharepoint_site_url, folder_relative_url
):
    """
    Uploads a local file to SharePoint.
    Uses environment variables for credentials: BI_SP_USER, BI_SP_PW

    :param local_file_path: str path to the local file
    :param sharepoint_site_url: str e.g. 'https://yourtenant.sharepoint.com/sites/YourSite'
    :param folder_relative_url: str e.g. '/sites/YourSite/Shared Documents/FolderName'
    :return: None
    """
    try:
        ctx = ClientContext(sharepoint_site_url).with_credentials(
            UserCredential(os.environ["BI_SP_USER"], os.environ["BI_SP_PW"])
        )
        with open(local_file_path, "rb") as file:
            file_content = file.read()
        # Filename is same as original file
        remote_file_name = os.path.basename(local_file_path)

        target_folder = ctx.web.get_folder_by_server_relative_url(folder_relative_url)
        target_folder.upload_file(remote_file_name, file_content)
        ctx.execute_query()

        get_logger().info(
            f"File uploaded successfully to SharePoint => {remote_file_name}"
        )

    except Exception as e:
        get_logger().error(
            f"Error uploading file to SharePoint: {e}\n{traceback.format_exc()}"
        )
        raise e


#######################
# Core Function
#######################


def create_new_excel_from_db(
    db_type,
    db_name,
    db_user,
    db_password,
    db_host,
    db_port,
    sql_query,
    base_filename,
    sharepoint_site_url,
    sharepoint_folder_relative_url,
):
    # 1. Create a new filename that includes today's month-day
    today_str = datetime.now().strftime("%m_%d")
    excel_file = f"{base_filename}_{today_str}.xlsx"

    try:
        if db_type.lower() == "postgresql":
            conn = psycopg2.connect(
                dbname=db_name,
                user=db_user,
                password=db_password,
                host=db_host,
                port=db_port,
            )
        elif db_type.lower() == "mssql":
            # Construct the connection string.
            # If db_host contains the named instance (e.g. "10.1.7.19\SAGE"), do not specify a port.
            connection_string = (
                "DRIVER={ODBC Driver 17 for SQL Server};"
                f"SERVER={db_host},{db_port};"
                f"DATABASE={db_name};"
                f"UID={db_user};"
                f"PWD={db_password};"
            )
            conn = pyodbc.connect(connection_string)
        else:
            raise ValueError(f"Unsupported db_type: {db_type}")

        cursor = conn.cursor()
        cursor.execute(sql_query)
        results = cursor.fetchall()

        if not results:
            get_logger().info("No data found for the specified query.")
            return

        column_names = [desc[0] for desc in cursor.description]

        workbook = Workbook()
        sheet = workbook.active

        # Write header row
        sheet.append(column_names)
        # Append rows of data
        for row in results:
            if db_type.lower() == "mssql":
                row = tuple(row)
            sheet.append(row)

        workbook.save(excel_file)
        get_logger().info(
            f"Data written to local Excel file: '{excel_file}' "
            f"(sheet: '{sheet.title}')."
        )

        # ==== Upload to SharePoint ====
        upload_excel_to_sharepoint(
            excel_file, sharepoint_site_url, sharepoint_folder_relative_url
        )

    except (psycopg2.Error, pyodbc.DatabaseError) as e:
        get_logger().error(f"Database error: {e}")
    except Exception as e:
        get_logger().error(f"Unexpected error: {e}\n{traceback.format_exc()}")
    finally:
        # Clean up file
        if os.path.exists(excel_file):
            os.remove(excel_file)
            get_logger().info(f"Local file removed: {excel_file}")
        if "conn" in locals() and conn:
            conn.close()


#######################
# Process Runner
#######################


def main():
    dimensions = {"ProcessName": "ExcelDBProcess"}

    # Set your SharePoint site and target folder
    sharepoint_base_url = "https://picanovagmbh.sharepoint.com/sites/AI-Team"
    sharepoint_folder_relative_url = (
        "/sites/AI-Team/Freigegebene Dokumente/Projects/Automations/Production Data"
    )

    start_time = time.time()
    try:
        get_metrics().increment_count("Process.Start", dimensions=dimensions)

        # Run Sku SQL
        create_new_excel_from_db(
            "postgresql",
            os.getenv("PCS_DB_NAME"),
            os.getenv("PCS_DB_USERNAME"),
            os.getenv("PCS_DB_PASSWORD"),
            os.getenv("PCS_DB_HOST"),
            5432,
            SKU_SQL,
            "SKU24h",
            sharepoint_base_url,
            sharepoint_folder_relative_url,
        )

        # Run Received Material SQL
        create_new_excel_from_db(
            "mssql",
            os.getenv("PRINTDREAM_DB_NAME"),
            os.getenv("PRINTDREAM_DB_USERNAME"),
            os.getenv("PRINTDREAM_DB_PASSWORD"),
            os.getenv("PRINTDREAM_DB_HOST"),
            os.getenv("PRINTDREAM_DB_PORT"),
            RECIEVED_MATERIAL,
            "ReceivedMaterial24h",
            sharepoint_base_url,
            sharepoint_folder_relative_url,
        )

        # Run Frames SQL
        create_new_excel_from_db(
            "postgresql",
            os.getenv("PCS_DB_NAME"),
            os.getenv("PCS_DB_USERNAME"),
            os.getenv("PCS_DB_PASSWORD"),
            os.getenv("PCS_DB_HOST"),
            5432,
            FRAMES_SQL,
            "Frames24h",
            sharepoint_base_url,
            sharepoint_folder_relative_url,
        )

        get_metrics().increment_count("Process.Success", dimensions=dimensions)
    except Exception as e:
        get_logger().error(f"Error in run_excel_db_process: {e}")
        get_metrics().increment_count("Process.Failure", dimensions=dimensions)
        get_metrics().record_error("Process.Error", dimensions=dimensions)
    finally:
        processing_time = (time.time() - start_time) * 1000  # ms
        get_metrics().record_timing(
            "Process.Duration", processing_time, dimensions=dimensions
        )
        get_logger().info(f"Process completed in {processing_time:.2f} ms")


#######################
# Main Entry Point
#######################

if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()