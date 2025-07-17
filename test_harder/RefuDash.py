"""
Refund Data Processing and SharePoint Integration Script

This script performs the following main tasks:
1. Downloads a RefundDataset Excel file from SharePoint.
2. Retrieves new refund data from a PostgreSQL database.
3. Merges the new data with the existing dataset.
4. Uploads the updated dataset back to SharePoint.
5. Runs continuously, updating the dataset every 30 minutes.

Key components:
- SharePoint Integration: Uses Office365 library for file download and upload.
- Database Operations: Executes SQL queries on a PostgreSQL database to fetch new refund data.
- Data Processing: Merges existing and new refund data using pandas.
- File Handling: Manages local Excel file operations.
- Timeout Handling: Implements custom timeout mechanisms for both Unix and Windows systems.

Environment Variables Required:
- SharePoint credentials (BI_SP_USER, BI_SP_PW)
- Database credentials (PICTURATOR_DB_USER, PICTURATOR_DB_PW, PICTURATOR_DB_HOST)
"""
import multiprocessing
import os
import signal
import sys
import threading
import time
from contextlib import contextmanager
from datetime import datetime, timedelta
from functools import wraps
from urllib.parse import urlencode
import urllib.parse

import openpyxl  # noqa: E402
import pandas as pd
import psycopg2
from aimetricslib import CloudWatchMetrics
from office365.runtime.auth.user_credential import UserCredential  # noqa: E402
from office365.sharepoint.client_context import ClientContext  # noqa: E402

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory
parent_dir = os.path.dirname(current_dir)

# Add the parent directory to the Python path
sys.path.append(parent_dir)

import no_secret_config  # noqa: F401, E402
from logger import LoggerRegistry  # noqa: E402

_logger = None
REFUND_DASHBOARD_METRIC_NAMESPACE = "Automation.RefundDashboard"


def get_logger():
    global _logger
    if _logger is None:
        _logger = LoggerRegistry.get_logger("local_schedule", "refund_dashboard")
    return _logger


def get_metrics():
    if not hasattr(get_metrics, "instance"):
        get_logger().info("Initializing CloudWatchMetrics client for Refund Dashboard.")
        get_metrics.instance = CloudWatchMetrics(
            namespace=REFUND_DASHBOARD_METRIC_NAMESPACE,
            region="eu-central-1",
            logger=get_logger(),
        )
    return get_metrics.instance


class TimeoutException(Exception):
    """Custom exception for timeout scenarios."""

    pass


# Unix specific timeout functions
def unix_timeout_handler(signum, frame):
    """Signal handler for Unix systems to raise TimeoutException."""
    raise TimeoutException


@contextmanager
def unix_time_limit(seconds):
    """
    Context manager to implement timeout for Unix systems.

    Args:
        seconds (int): Number of seconds before timeout.

    Raises:
        TimeoutException: If the time limit is exceeded.
    """
    signal.signal(signal.SIGALRM, unix_timeout_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)


# Windows specific timeout functions
def windows_run_with_timeout(func, args=(), kwargs=None, timeout_duration=600):
    """
    Run a function with a timeout for Windows systems.

    Args:
        func (callable): The function to run.
        args (tuple): Positional arguments for the function.
        kwargs (dict): Keyword arguments for the function.
        timeout_duration (int): Number of seconds before timeout.

    Returns:
        The result of the function.

    Raises:
        TimeoutException: If the function doesn't complete within the timeout.
    """
    if kwargs is None:
        kwargs = {}
    result = [None]

    def func_wrapper():
        result[0] = func(*args, **kwargs)

    thread = threading.Thread(target=func_wrapper)
    thread.start()
    thread.join(timeout_duration)

    if thread.is_alive():
        raise TimeoutException("Function timed out")
    else:
        return result[0]


# Wrapper to detect OS and apply the correct timeout method
def timeout(seconds):
    """
    Decorator to apply timeout to a function, compatible with both Unix and Windows.

    Args:
        seconds (int): Number of seconds before timeout.

    Returns:
        function: Decorated function with timeout mechanism.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if sys.platform == "win32":
                return windows_run_with_timeout(func, args, kwargs, seconds)
            else:
                with unix_time_limit(seconds):
                    return func(*args, **kwargs)

        return wrapper

    return decorator


def get_sharepoint_file(site_url, relative_url, fname):
    """
    Download a file from SharePoint.

    Args:
        site_url (str): The SharePoint site URL.
        relative_url (str): The relative URL of the file in SharePoint.
        fname (str): The name to save the file as locally.

    Returns:
        bool: True if download was successful, False otherwise.
    """
    try:
        ctx = ClientContext(site_url).with_credentials(
            UserCredential(os.environ["BI_SP_USER"], os.environ["BI_SP_PW"])
        )
        file = ctx.web.get_file_by_server_relative_url(relative_url)
        response = file.open_binary_stream()
        ctx.execute_query()
        with open(fname, "wb") as local_file:
            buffer = response.value  # Read the binary stream
            local_file.write(buffer)
        get_logger().info(f"Refund Dashboard File downloaded successfully - {fname}")
        return True
    except Exception as e:
        get_logger().error(f"Error: Refund Dashboard {e}")
        return False


@timeout(60)
def upload_sharepoint_file(site_url, relative_url, local_file_path):
    """
    Upload a file to SharePoint with a 60-second timeout.

    Args:
        site_url (str): The SharePoint site URL.
        relative_url (str): The relative URL where the file should be uploaded in SharePoint.
        local_file_path (str): The local path of the file to upload.

    Returns:
        bool: True if upload was successful, False otherwise.
    """
    try:
        # Connect to SharePoint
        ctx = ClientContext(site_url).with_credentials(
            UserCredential(os.environ["BI_SP_USER"], os.environ["BI_SP_PW"])
        )

        # Read the file content
        with open(local_file_path, "rb") as local_file:
            file_content = local_file.read()

        # Get the folder by server relative URL
        folder_url = "/".join(relative_url.split("/")[:-1])
        folder = ctx.web.get_folder_by_server_relative_url(folder_url)
        ctx.load(folder)
        ctx.execute_query()

        # Upload the file to SharePoint
        file_name = relative_url.split("/")[-1]
        folder.upload_file(file_name, file_content)
        ctx.execute_query()

        get_logger().info(
            f"Refund Dashboard File uploaded successfully - {local_file_path}"
        )
        return True
    except Exception as e:
        get_logger().error(f"Refund Dashboard Error: {e}")
        return False


def dload_data_p(qry):
    """
    Execute a query on the PostgreSQL database and return the results.

    Args:
        qry (str): SQL query to execute.

    Returns:
        list: Query results as a list of tuples.
    """
    connection = psycopg2.connect(
        user=os.environ["PICTURATOR_DB_USER"],
        password=os.environ["PICTURATOR_DB_PW"],
        host=os.environ["PICTURATOR_DB_HOST"],
        port="5432",
        database="picturator",
    )
    cursor = connection.cursor()
    cursor.execute(qry)
    pict_data = cursor.fetchall()
    cursor.close()
    connection.close()
    return pict_data


def construct_refund_url(access_code, order_number, refund_id):
    """
    Construct the refund URL.

    Args:
        access_code (str): The access code for the order.
        order_number (str): The order number.
        refund_id (str): The refund ID.

    Returns:
        str: The constructed refund URL.
    """
    params = {
        "accessCode": access_code,
        "orderNumber": order_number,
        "refundId": refund_id,
    }
    return f"https://testing-my-picture-co-uk.picanova.de/api/downloadRefundInvoice?{urlencode(params)}"


def download_file(site_url, relative_url, local_filename):
    """
    Downloads the SharePoint file and returns the dataframe.
    """
    get_logger().info(f"Starting download for {local_filename}")
    download_time = download_sharepoint_file(site_url, relative_url, local_filename)
    get_logger().info(f"Downloaded {local_filename} successfully")
    return pd.read_excel(local_filename, sheet_name="Sheet1")


def process_max_date(rdf, dataset_name):
    """
    Process the max date for the given dataset and handle errors.
    Falls back to a date 7 days before today if no valid date is found.
    """
    try:
        # Ensure the column is in datetime format
        get_logger().info(f"Converting 'Date of Refund' column to datetime for {dataset_name}.")
        rdf["Date of Refund"] = pd.to_datetime(rdf["Date of Refund"], errors="coerce")

        max_date = rdf["Date of Refund"].max()
        max_date = max_date.strftime("%Y-%m-%d")
        get_logger().info(f"Processed max date for {dataset_name}: {max_date}")
        return max_date
    except Exception as e:
        get_logger().error(f"Refund Dashboard Error in process_max_date for {dataset_name}: {e}")
        # Fallback to 7 days before today
        fallback_date = (pd.Timestamp.now() - pd.Timedelta(days=7)).strftime("%Y-%m-%d")
        get_logger().warning(f"Using fallback date: {fallback_date} for {dataset_name}")
        return fallback_date


def fetch_and_merge_data(rdf, max_date, dataset_name):
    """
    Fetch new data and merge it with the existing dataframe.
    """
    get_logger().info(f"Fetching new refund data for {dataset_name} with max date: {max_date}")
    db_data = fetch_data_from_database(max_date)
    get_logger().info(f"Merging new data for {dataset_name}")
    return filter_and_merge_new_data(rdf, db_data)


def upload_file(rdf, filename, site_url, relative_url):
    """
    Uploads the file to SharePoint.
    """
    get_logger().info(f"Uploading updated {filename} to SharePoint")
    upload_to_sharepoint(rdf, filename, site_url, relative_url)
    get_logger().info(f"Uploaded {filename} to SharePoint")


def remove_local_file(filename):
    """
    Removes local file after processing.
    """
    remove_local_file(filename)
    get_logger().info(f"Cleaned up local file {filename}")


def do_all(process_first=True, process_second=True):
    """
    Main function to orchestrate all tasks: download files, fetch new data, merge, and upload.
    Processes both 'Refund Dataset' and 'Refund Dataset_v2' based on flags.
    """
    dimensions = {"Process": "RefundDashboard"}
    site_url_1 = "https://picanovagmbh-my.sharepoint.com/personal/bi_picanova_picanova_com"
    site_url_2 = "https://picanovagmbh.sharepoint.com/sites/AI-Team"

    try:
        # Step 1: Conditional Download SharePoint Files based on flags
        rdf_1 = None
        rdf_2 = None

        if process_first:
            rdf_1 = download_file(site_url_1,
                                  "/personal/bi_picanova_picanova_com/Documents/RefundDataset.xlsx",
                                  "RefundDataset.xlsx")

        if process_second:
            rdf_2 = download_file(site_url_2,
                                  "/sites/AI-Team/Freigegebene Dokumente/Refund Dashboard/Refund dataset/Refund Dataset_v2.xlsx",
                                  "Refund Dataset_v2.xlsx")

        # Step 2: Process Max Dates for both datasets
        max_date_1 = process_max_date(rdf_1, "rdf_1") if rdf_1 is not None else None
        max_date_2 = process_max_date(rdf_2, "rdf_2") if rdf_2 is not None else None

        # Step 3: Fetch and merge new data for both datasets
        if process_first and rdf_1 is not None:
            rdf_1 = fetch_and_merge_data(rdf_1, max_date_1, "rdf_1")

        if process_second and rdf_2 is not None:
            rdf_2 = fetch_and_merge_data(rdf_2, max_date_2, "rdf_2")

        # Step 4: Upload Updated Files to SharePoint
        if process_first and rdf_1 is not None:
            upload_file(rdf_1, "RefundDataset.xlsx", site_url_1,
                        "/personal/bi_picanova_picanova_com/Documents/RefundDataset.xlsx")

        if process_second and rdf_2 is not None:
            upload_file(rdf_2, "Refund Dataset_v2.xlsx", site_url_2,
                        "/sites/AI-Team/Freigegebene Dokumente/Refund Dashboard/Refund dataset/Refund Dataset_v2.xlsx")

        # Step 5: Clean up local files
        if process_first and rdf_1 is not None:
            remove_local_file("RefundDataset.xlsx")

        if process_second and rdf_2 is not None:
            remove_local_file("Refund Dataset_v2.xlsx")

        # Log success
        get_metrics().increment_count("Process.Success", dimensions=dimensions)
        get_logger().info("Process completed successfully")

    except Exception as e:
        get_logger().error(f"Error during process: {e}")
        get_metrics().increment_count("Process.Failure", dimensions=dimensions)
        get_metrics().record_error("Process.Error", dimensions=dimensions)
        get_logger().error("Process failed with error")


def download_sharepoint_file(site_url, relative_url, local_file_path):
    """
    Downloads a file from SharePoint.
    """
    get_logger().info(f"Starting to download {local_file_path}")
    encoded_url = urllib.parse.quote(relative_url, safe="/")
    _done = get_sharepoint_file(site_url, encoded_url, local_file_path)
    if not _done:
        raise Exception(f"Failed to download {local_file_path} from SharePoint")
    get_metrics().increment_count("SharePoint.Download.Success", dimensions={"Process": "RefundDashboard"})
    return time.time()


def fetch_data_from_database(max_date):
    """
    Executes SQL query to fetch refund data from the database.
    """
    qry = f"""
    SELECT
        p.ordernumber "Order ID",
        p.paymenttransactionid "Transaction ID",
        p.paymentmethod "Payment Provider",
        r.created::date "Date of Refund",
        u.login "Initiated by (CS-Agent)",
        refund_amount "Amount to be refunded",
        c.code "Currency",
        r.id "Refund ID",
        p.accesscode "Access Code",
        p.paymentreferenceid "Payment Reference ID"
    FROM public.refunds r
    LEFT JOIN (SELECT SUM(amount) refund_amount, refundid FROM public.refunditems GROUP BY refundid) ti ON ti.refundid=r.id
    LEFT JOIN public.orders p ON p.id=r.orderid
    LEFT JOIN public.users u ON u.id=r.userid
    LEFT JOIN public.currencies c ON c.id=p.currencyid
    WHERE r.created::date >= '2024-05-20'
    AND r.created::date >= '{max_date}'
    AND p.paymenttransactionid IS NOT NULL
    AND p.paymenttransactionid != ''
    ORDER BY r.created ASC
    """
    return pd.DataFrame(dload_data_p(qry), columns=[
        "Order ID", "Transaction ID", "Payment Provider", "Date of Refund",
        "Initiated by (CS-Agent)", "Amount to be refunded", "Currency",
        "Refund ID", "Access Code", "Payment Reference ID"
    ])


def filter_and_merge_new_data(rdf, db_data):
    """
    Filters and merges new refund data with the existing data (rdf).
    """
    df_new = db_data[~db_data["Order ID"].isin(rdf["Order ID"])].copy()
    df_new["Refund URL"] = df_new.apply(
        lambda row: construct_refund_url(row["Access Code"], row["Order ID"], row["Refund ID"]),
        axis=1,
    )
    df_new = df_new.drop(columns=["Access Code", "Refund ID"])
    return pd.concat([rdf, df_new], ignore_index=True)


def upload_to_sharepoint(rdf, local_file, site_url, relative_url):
    """
    Uploads the updated file to SharePoint.
    """
    with pd.ExcelWriter(local_file, engine="openpyxl", mode="w") as writer:
        rdf.to_excel(writer, sheet_name="Sheet1", index=False)
    _uploaded = upload_sharepoint_file(site_url, relative_url, local_file)
    if not _uploaded:
        get_logger().error(f"Failed to upload {local_file} to SharePoint")
    get_metrics().increment_count("SharePoint.Upload.Success", dimensions={"Process": "RefundDashboard"})


def remove_local_file(file_path):
    """
    Removes a local file after processing.
    """
    os.remove(file_path)


def get_berlin_time():
    return datetime.utcnow() + timedelta(hours=1)


def main():
    """
    The script enters an infinite loop, calling do_all() function every 30 minutes.
    This ensures continuous updating of the refund dataset with new data from the database.
    """
    dimensions = {"Process": "RefundDashboard"}
    while True:
        berlin_time = get_berlin_time()
        current_hour = berlin_time.hour

        # Run only during office hours (7 AM to 7 PM Berlin time) / non-peak DB hours.
        if 7 <= current_hour < 19:
            get_logger().info("Starting refund dashboard process.")
            start_time = time.time()

            try:
                do_all(True, True)
                execution_time = (time.time() - start_time) * 1000
                get_metrics().record_timing(
                    "Process.ExecutionTime", execution_time, dimensions=dimensions
                )
            except Exception as e:
                get_logger().error(f"Error during refund dashboard execution: {e}")
                get_metrics().increment_count("Process.Failure", dimensions=dimensions)
        else:
            get_logger().info("Outside office hours, skipping execution.")
            get_metrics().increment_count("Process.Skipped", dimensions=dimensions)

        get_logger().info("Refund Dashboard sleeping for 30 minutes")
        time.sleep(60 * 30)


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()