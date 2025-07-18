import io
import multiprocessing
import os
import sys
import time
import traceback
from datetime import datetime, timedelta

import openpyxl
import pandas as pd
from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.file import File
from WarehouseStockAlertsData.frames_data import FRAMES  # noqa: F401, E402
from WarehouseStockAlertsData.items_data import ITEMS  # noqa: F401, E402

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
# Get the parent directory
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from aimetricslib import CloudWatchMetrics  # noqa: E402

import no_secret_config  # noqa: F401, E402
from logger import LoggerRegistry  # noqa: E402

#######################
# Logging & Metrics
#######################

_logger = None


def get_logger():
    """
    Lazy-initializes and returns the global logger.
    """
    global _logger
    if _logger is None:
        # TODO create logger in aws
        _logger = LoggerRegistry.get_general_logger("warehouse_stock_alerts")
    return _logger


def get_metrics():
    """
    Lazy-initializes and returns the CloudWatchMetrics client.
    """
    if not hasattr(get_metrics, "instance"):
        get_logger().info(
            "Initializing CloudWatchMetrics client for Warehouse Stock Alerts process."
        )
        get_metrics.instance = CloudWatchMetrics(
            namespace="Automation.WarehouseStockAlerts",
            region="eu-central-1",
            logger=get_logger(),
        )
    return get_metrics.instance


#######################
# Core Function
#######################


def update_items_inventory(
    received_df: pd.DataFrame,
    production_df: pd.DataFrame,
    master_stock_file_active_sheet: openpyxl.worksheet.worksheet.Worksheet,
):
    # For each item: calculate new stock, print, then write to Excel
    for info in ITEMS.values():
        # 1. Sum of received
        if received_df:
            received_qty = received_df[received_df["barcode"].isin(info["barcodes"])][
                "qty"
            ].sum()
        else:
            received_qty = 0

        # 2. Sum of used (depends on whether we have "sku_usage" or "skus")
        used_qty = 0

        if production_df:
            if "sku_usage" in info:
                # "sku_usage" is a dict of {sku: usage_factor}
                for sku, factor in info["sku_usage"].items():
                    # How many units of this SKU were produced?
                    produced_qty = production_df.loc[
                        production_df["sku"] == sku, "qty"
                    ].sum()
                    used_qty += produced_qty * factor
            elif "skus" in info:
                # "skus" is just a list with a usage factor of 1 each
                produced_qty = production_df.loc[
                    production_df["sku"].isin(info["skus"]), "qty"
                ].sum()
                used_qty = produced_qty  # 1:1 usage
        else:
            # No SKUs defined, fallback or skip
            used_qty = 0

        # 3. Current stock (from the cell in master stock)
        current_stock = ExcelUtils.get_float_value(
            master_stock_file_active_sheet[info["cell"]]
        )

        # 4. Compute new stock
        new_stock = current_stock + received_qty - used_qty

        # 5. Print for debugging
        get_logger().info(f"New stock for {info['name']}: {new_stock}")

        # 6. Write updated stock to Excel
        master_stock_file_active_sheet[info["cell"]] = new_stock


def update_frames_inventory(
    frames_df: pd.DataFrame,
    received_df: pd.DataFrame,
    master_stock_file_active_sheet: openpyxl.worksheet.worksheet.Worksheet,
):
    for _, frame_info in FRAMES.items():
        if frames_df is not None:
            # 5.1. Filter the frames DataFrame by "frame_type" and "frame_siz
            df_filtered = frames_df[
                (frames_df["FrameType"] == frame_info["frame_type"])
                & (frames_df["FrameSize"] == frame_info["frame_size"])
            ]

            # 5.2. Sum the "ProducedQty" in those filtered rows
            used_qty = df_filtered["ProducedQty"].sum()
        else:
            used_qty = 0

        if received_df is not None and "barcodes" in frame_info:
            frames_received_qty = received_df[
                received_df["barcode"].isin(frame_info["barcodes"])
            ]["qty"].sum()
        else:
            frames_received_qty = 0

        # Current stock from the master
        current_stock = ExcelUtils.get_float_value(
            master_stock_file_active_sheet[frame_info["cell"]]
        )

        new_stock = current_stock + frames_received_qty - used_qty

        # 5.3. Print for debugging
        get_logger().info(f"{frame_info['name']} leftover stock: {new_stock}")

        # 5.4. Write the usage to the specified cell in the master
        master_stock_file_active_sheet[frame_info["cell"]] = new_stock


def process_received_data(received_file_buffer: io.IOBase) -> pd.DataFrame:
    """Process received items data"""
    received_df = ExcelUtils.read_excel_buffer(received_file_buffer, usecols="B,E")
    received_df.columns = ["barcode", "qty"]
    return received_df


def process_production_data(production_file_buffer: io.BytesIO) -> pd.DataFrame:
    """Process production data"""
    production_df = ExcelUtils.read_excel_buffer(production_file_buffer, usecols="A,B")
    production_df.columns = ["qty", "sku"]
    return production_df


def process_frames_data(frames_file_buffer: io.BytesIO) -> pd.DataFrame:
    """Process frames data"""
    frames_df = ExcelUtils.read_excel_buffer(frames_file_buffer, usecols="A,C,D")
    frames_df.columns = ["ProducedQty", "FrameType", "FrameSize"]
    return frames_df


def get_received_data(received_file_name: str) -> pd.DataFrame:
    received_file_buffer = None
    try:
        received_file_buffer = SharePointClient.get_sharepoint_file_io_buffer(
            file_name=received_file_name
        )
        return process_received_data(received_file_buffer)
    except Exception:
        return None
    finally:
        if received_file_buffer:
            received_file_buffer.close()


def get_production_data(production_file_name: str) -> pd.DataFrame:
    production_file_buffer = None
    try:
        production_file_buffer = SharePointClient.get_sharepoint_file_io_buffer(
            file_name=production_file_name
        )
        return process_production_data(production_file_buffer)
    except Exception:
        return None
    finally:
        if production_file_buffer:
            production_file_buffer.close()


def get_frames_data(frames_file_name: str) -> pd.DataFrame:
    frames_file_buffer = None
    try:
        frames_file_buffer = SharePointClient.get_sharepoint_file_io_buffer(
            file_name=frames_file_name
        )
        return process_frames_data(frames_file_buffer)
    except Exception:
        return None
    finally:
        if frames_file_buffer:
            frames_file_buffer.close()


def main(target_date: str = None):
    """
    Main function to update warehouse stock alerts.
    Args:
        target_date (str, optional): The reference date in the format "dd-mm-yyyy".
                                     Defaults to None, which uses the current date.
    Returns:
        None
    """

    dimensions = {"ProcessName": "WarehouseStockAlerts"}

    # Initialize buffers
    master_stock_file_buffer = None
    output_buffer = None

    start_time = time.time()
    try:
        # If you track metrics, presumably from your environment:
        get_metrics().increment_count("Process.Start", dimensions=dimensions)

        # Use given target_date or fall back to today
        if target_date:
            reference_date = datetime.strptime(target_date, "%d-%m-%Y")
        else:
            reference_date = datetime.now()

        get_logger().info(
            f"[Warehouse Stock Alerts] Process started for reference date: '{reference_date}'"
        )

        today_str = reference_date.strftime("%m_%d")
        yesterday_str = (reference_date - timedelta(days=1)).strftime("%m_%d")

        # Define file paths
        received_file_name = f"ReceivedMaterial24h_{today_str}.xlsx"
        production_file_name = f"SKU24h_{today_str}.xlsx"
        frames_file_name = f"Frames24h_{today_str}.xlsx"
        master_stock_name = f"testStock{yesterday_str}.xlsx"
        # Create an output file name with today's month/day
        output_master_stock_name = f"testStock{today_str}.xlsx"

        master_stock_file_buffer = SharePointClient.get_sharepoint_file_io_buffer(
            file_name=master_stock_name
        )
        # Load the master stock workbook and select active sheet
        master_stock_file_workbook = openpyxl.load_workbook(
            master_stock_file_buffer, data_only=True
        )
        master_stock_file_active_sheet = master_stock_file_workbook.active

        received_df = get_received_data(received_file_name=received_file_name)
        production_df = get_production_data(production_file_name=production_file_name)

        update_items_inventory(
            received_df, production_df, master_stock_file_active_sheet
        )

        frames_df = get_frames_data(frames_file_name=frames_file_name)
        update_frames_inventory(frames_df, received_df, master_stock_file_active_sheet)

        # Save the updated workbook to a buffer
        output_buffer = io.BytesIO()
        master_stock_file_workbook.save(output_buffer)
        output_buffer.seek(0)

        # -------- Upload the updated workbook to SharePoint
        SharePointClient.upload_file_buffer_to_sharepoint(
            file_buffer=output_buffer, file_name=output_master_stock_name
        )

        get_metrics().increment_count("Process.Success", dimensions=dimensions)

    except Exception as e:
        get_logger().error(f"Error running Warehouse Stock Alerts automation: {e}")
        get_metrics().increment_count("Process.Failure", dimensions=dimensions)
        get_metrics().record_error("Process.Error", dimensions=dimensions)
    finally:
        processing_time = (time.time() - start_time) * 1000  # ms
        get_metrics().record_timing(
            "Process.Duration", processing_time, dimensions=dimensions
        )

        # Close all buffers if they exist
        if master_stock_file_buffer:
            master_stock_file_buffer.close()
        if output_buffer:
            output_buffer.close()

        get_logger().info(
            f"[Warehouse Stock Alerts] Process completed in {processing_time:.2f} ms. reference date: '{reference_date}'"
        )


class ExcelUtils:
    @staticmethod
    def read_excel_file_buffer(
        file_buffer: io.BytesIO, **pandas_kwargs
    ) -> pd.DataFrame:
        """
        Read a SharePoint Excel file into a pandas DataFrame

        Args:
            sharepoint_base_url (str): The base URL of the SharePoint site
            file_relative_url (str): The server relative URL of the Excel file
            **pandas_kwargs: Additional arguments to pass to pandas.read_excel()

        Returns:
            pandas.DataFrame or None: The DataFrame if successful, None otherwise
        """

        if file_buffer is None:
            raise ValueError("The file buffer is None.")

        try:
            df = pd.read_excel(file_buffer, **pandas_kwargs)
            return df
        except Exception as e:
            get_logger().error(
                f"Error reading Excel file: {e}\nTraceback:\n{traceback.format_exc()}"
            )
            raise e

    # Helper function to safely convert a cell value to float
    @staticmethod
    def get_float_value(cell):
        try:
            return float(cell.value)
        except (TypeError, ValueError):
            return 0.0


class SharePointClient:
    # Set your SharePoint site and target folder
    sharepoint_base_url = "https://picanovagmbh.sharepoint.com/sites/AI-Team"
    sharepoint_folder_relative_url = (
        "/sites/AI-Team/Freigegebene Dokumente/Projects/Automations/Production Data"
    )

    @staticmethod
    def get_credentials() -> UserCredential:
        """Get SharePoint credentials from environment variables"""
        return UserCredential(os.environ["BI_SP_USER"], os.environ["BI_SP_PW"])

    @classmethod
    def get_sharepoint_file_io_buffer(cls, file_name: str) -> io.BytesIO:
        """
        Download a file from SharePoint and save it locally.

        Args:
            file_relative_url (str): The relative URL of the file within the SharePoint site. Ex: "/sites/yoursite/Shared Documents/yourfile.xlsx".

        Returns:
            tuple: Full path of the downloaded file (str)
        """
        try:
            file_relative_url = f"{cls.sharepoint_folder_relative_url}/{file_name}"

            credentials = cls.get_credentials()
            ctx = ClientContext(cls.sharepoint_base_url).with_credentials(
                credentials=credentials
            )

            file = ctx.web.get_file_by_server_relative_url(file_relative_url)
            ctx.load(file)
            ctx.execute_query()

            # Download file content to memory
            response = File.open_binary(ctx, file_relative_url)
            get_logger().info(
                f"File buffer downloaded from SharePoint: {file_relative_url}"
            )
            return io.BytesIO(response.content)

        except Exception as e:
            get_logger().error(
                f"Error downloading file from SharePoint: {e}\nTraceback:\n{traceback.format_exc()}"
            )
            raise e

    @classmethod
    def upload_file_buffer_to_sharepoint(cls, file_buffer: io.BytesIO, file_name: str):
        """
        Uploads a local file to SharePoint.
        Uses environment variables for credentials: BI_SP_USER, BI_SP_PW

        Args:
            file_buffer: io.BytesIO
            file_relative_url: str e.g. '/sites/YourSite/Shared Documents/FolderName/filename'
        Returns:
            None
        """
        try:
            file_relative_url = f"{cls.sharepoint_folder_relative_url}/{file_name}"

            credentials = cls.get_credentials()
            ctx = ClientContext(cls.sharepoint_base_url).with_credentials(
                credentials=credentials
            )

            target_folder = ctx.web.get_folder_by_server_relative_url(file_relative_url)
            target_folder.upload_file(file_relative_url, file_buffer)
            ctx.execute_query()

            get_logger().info(
                f"File buffer uploaded successfully to SharePoint => {file_relative_url}"
            )

        except Exception as e:
            get_logger().error(
                f"Error uploading file to SharePoint: {e}\n{traceback.format_exc()}"
            )
            raise e


#######################
# Main Entry Point
#######################
if __name__ == "__main__":
    multiprocessing.freeze_support()
    get_logger().info("Starting Warehouse Stock Alerts in manual mode")
    main()
    # main("31-03-2025")
    # Or call main("26-02-2025") for testing a custom date