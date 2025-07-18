# test_harder

## Overview
The `test_harder` folder contains Python scripts that are part of the project's testing and database management functionalities.

## Structure
The folder consists of three Python files:
- RefuDash.py: Contains code related to testing and quality assurance.
- Translate.py: Handles translation functions for the project.
- WareHouseDB.py: Manages interactions with the project's database.

## Key Files
- RefuDash.py: This file is crucial for running tests and ensuring the quality of the project's code.
- WareHouseDB.py: Important for managing database operations and ensuring data integrity.

## Usage
1. To run tests using RefuDash.py, execute the script with appropriate parameters.
2. Utilize Translate.py for any translation-related tasks in the project.
3. Make use of WareHouseDB.py for database interactions and management.

---

# Files Documentation

## RefuDash.py

**Purpose:** This script handles the processing of refund data by integrating with SharePoint, fetching data from a PostgreSQL database, merging datasets, and updating the SharePoint file periodically.

**Key Components:**
- SharePoint Integration: Utilizes the Office365 library for downloading and uploading files from SharePoint.
- Database Operations: Executes SQL queries on a PostgreSQL database to retrieve new refund data.
- Data Processing: Merges existing and new refund data using the pandas library.
- File Handling: Manages local Excel file operations.
- Timeout Handling: Implements custom timeout mechanisms for Unix and Windows systems.

**Usage:** This script can be run continuously to automate the process of updating refund data on SharePoint. Ensure that the required environment variables for SharePoint and the database are set before running the script.

**Dependencies:**
- `multiprocessing`
- `os`
- `signal`
- `sys`
- `threading`
- `time`
- `contextlib`
- `datetime`
- `functools`
- `urllib.parse`
- `openpyxl`
- `pandas`
- `psycopg2`
- `aimetricslib` (Assumed to be a custom library)
- `office365`
- `no_secret_config` (Assumed to contain sensitive configuration information)
- `logger` (Assumed to be a custom logging module)

## Translate.py

**Purpose:** This script automates the process of retrieving, translating, and storing survey feedback from various sources using the DeepL API and a Redshift database. It handles different types of surveys and utilizes multithreading for improved performance.

**Key Components:**
- `get_logger()`: Function to retrieve a logger instance for logging.
- `dload_data(qry)`: Function to download data from a Redshift database using a provided SQL query.
- `do_translation(text, lang)`: Function to translate text to English using the DeepL API.
- `insert_data(data, table, columns)`: Function to insert data into a specified table in the database.

**Usage:** This file can be imported into other scripts for automating survey feedback translation and processing tasks.

**Dependencies:**
- pandas
- redshift_connector
- deepl

Environment variables required:
- BI_DB_HOST: Redshift database host
- BI_DB_USER: Redshift database user
- BI_DB_PASS: Redshift database password
- DEEPL_API_KEY: DeepL API key for translations

Note: This script assumes the existence of a local configuration file 'no_secret_config.py' in a specific directory.

## WareHouseDB.py

**Purpose:** This Python file contains SQL queries related to warehouse operations and defines a logger for logging and metrics.

**Key Components:**
- `SKU_SQL`: SQL query to retrieve SKU information based on certain conditions.
- `RECIEVED_MATERIAL`: SQL query to retrieve information about received materials.
- `FRAMES_SQL`: SQL query to retrieve frame information based on certain conditions.
- `get_logger()`: Function to lazy-initialize and return the global logger.

**Usage:** This file can be imported to access the defined SQL queries and the `get_logger()` function for logging and metrics purposes.

**Dependencies:**
- `multiprocessing`
- `os`
- `sys`
- `time`
- `traceback`
- `datetime`
- `psycopg2`
- `pyodbc`
- `aimetricslib.CloudWatchMetrics`
- `office365.runtime.auth.user_credential.UserCredential`
- `office365.sharepoint.client_context.ClientContext`
- `openpyxl.Workbook`
- `no_secret_config`
- `logger.LoggerRegistry`

---
*Auto-generated documentation - Last updated: 2025-07-18 09:58:08*
