"""
Survey Translation and Processing Script

This script automates the process of retrieving, translating, and storing survey feedback
from various sources. It connects to a Redshift database, fetches untranslated survey
responses, translates non-English responses to English using the DeepL API, and then
stores the translated responses back in the database.

The script uses multithreading to improve performance when processing multiple survey
responses. It handles different types of surveys including Fulfillment, Shop, Help,
Relationship, and Feedback button surveys.

Dependencies:
- pandas
- redshift_connector
- deepl

Environment variables required:
- BI_DB_HOST: Redshift database host
- BI_DB_USER: Redshift database user
- BI_DB_PASS: Redshift database password
- DEEPL_API_KEY: DeepL API key for translations

Note: This script assumes the existence of a local configuration file 'no_secret_config.py'
in a specific directory.
"""

import multiprocessing
import os
import sys
import threading
from concurrent.futures import ThreadPoolExecutor

import deepl
import pandas as pd
import redshift_connector

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory
parent_dir = os.path.dirname(current_dir)

# Add the parent directory to the Python path
sys.path.append(parent_dir)
import no_secret_config  # noqa: F401, E402
from logger import LoggerRegistry  # noqa: E402

_logger = None


def get_logger():
    global _logger
    if _logger is None:
        _logger = LoggerRegistry.get_logger("local_schedule", "translate_cx")
    return _logger


def dload_data(qry):
    """
    Download data from Redshift database using the provided SQL query.

    Args:
        qry (str): SQL query to execute.

    Returns:
        pd.DataFrame: DataFrame containing the query results.
    """
    mydb = redshift_connector.connect(
        host=os.environ["BI_DB_HOST"],
        database="bi_stage_dev",
        user=os.environ["BI_DB_USER"],
        password=os.environ["BI_DB_PASS"],
        port=5439,
    )
    mycursor = mydb.cursor()
    mycursor.execute(qry)
    data: pd.DataFrame = mycursor.fetch_dataframe()
    mycursor.close()
    mydb.close()
    return data


def do_translation(text, lang):
    """
    Translate the given text to English using DeepL API.

    Args:
        text (str): Text to translate.
        lang (str): Source language code.

    Returns:
        str: Translated text in English or original text if translation fails.
    """
    if lang == "EN":
        return text
    try_no = 1
    while try_no < 4:
        try:
            translator = deepl.Translator(os.environ["DEEPL_API_KEY"])
            result = translator.translate_text(text, target_lang="EN-GB")
            return result.text
        except Exception as e:
            get_logger().error(f"Error: {e}")
            try_no += 1
    return text


def insert_data(data, table, columns):
    """
    Insert data into the specified Redshift table.

    Args:
        data (pd.DataFrame): DataFrame containing the data to insert.
        table (str): Name of the table to insert data into.
        columns (list): List of column names for insertion.
    """
    mydb = redshift_connector.connect(
        host=os.environ["BI_DB_HOST"],
        database="bi_stage_dev",
        user=os.environ["BI_DB_USER"],
        password=os.environ["BI_DB_PASS"],
        port=5439,
    )
    mycursor = mydb.cursor()
    column_names = ", ".join([f'"{col}"' for col in columns])
    placeholders = ", ".join(["%s"] * len(columns))
    query = f"""
        INSERT INTO {table} ({column_names})
        VALUES ({placeholders})
    """
    for row in data.itertuples(index=False):
        params = tuple(row[data.columns.get_loc(col)] for col in columns)
        mycursor.execute(query, params)

    mydb.commit()
    mycursor.close()
    mydb.close()


"""
SQL QUERY:
This SQL query aggregates feedback data from multiple survey sources dated from May 1, 2024, onward, with non-trivial content.
It unifies responses across various survey types into a single dataset and filters for those without existing translations, ensuring only unique, untranslated feedback is selected for further processing.
"""
qry = """with ss as (
                select f.response_id id,f.overall_feedback reason, 'Fulfillment' survey_type,q_language lang
                from bi_stage_dev_dbo.qualtrics_surveys_tnps_f f
                where f.start_date::Date>='2024-05-01' and length(f.overall_feedback)>0
                union all
                select f.response_id id,f.nps_reason reason, 'Shop' survey_type,user_language lang
                from bi_stage_dev_dbo.qualtrics_surveys_tnps_s f
                where f.start_date::Date>='2024-05-01' and length(f.nps_reason)>0
                union all
                select f.response_id id,f.nps_reason reason, 'Help' survey_type,user_language lang
                from bi_stage_dev_dbo.qualtrics_surveys_tnps_h f
                where f.start_date::Date>='2024-05-01' and length(f.nps_reason)>0
                union all
                select f.responseid id,f.nps_reason reason, 'Help Relaunch' survey_type,userlanguage lang
                from bi_stage_dev_dbo.qualtrics_surveys_tnps_h_relaunch f
                where f.startdate::Date>='2024-05-01' and length(f.nps_reason)>0
                union all
                select f.response_id id,f.nps_reason reason, 'Relationship' survey_type,user_language lang
                from bi_stage_dev_dbo.qualtrics_surveys_tnps_r f
                where f.start_date::Date>='2024-05-01' and length(f.nps_reason)>0
                union all
                select f.response_id id,f.technical_issue+' '+f.nps_reason reason, 'Feedback button' survey_type,user_language lang
                from bi_stage_dev_dbo.qualtrics_surveys_tnps_gfb f
                where f.start_date::Date>='2024-05-01' and length(f.technical_issue+' '+f.nps_reason)>1
                union all
                select f.response_id id,f.technical_issue+' '+f.nps_reason reason, 'Feedback button' survey_type,user_language lang
                from bi_stage_dev_dbo.qualtrics_surveys_tnps_gfb_old f
                where f.start_date::Date>='2024-05-01' and length(f.technical_issue+' '+f.nps_reason)>1
                )
            select
            distinct x.id,x.reason,x.lang
            from ss x
            left join (select distinct response_id xid from bi_stage_dev_dbo.qualtrics_translations) t on t.xid=x.id
            where t.xid is null
            """

df = dload_data(qry)


def process_move(df, i, list_lock, idx, translation):
    """
    Process a single survey response: translate and store the result.

    This function is designed to be used with ThreadPoolExecutor for parallel processing.

    Args:
        df (pd.DataFrame): DataFrame containing survey responses.
        i (int): Index of the row to process in the DataFrame.
    """

    response_id = df.id[i]
    text = df.reason[i]
    lang = df.lang[i]

    trans = do_translation(text, lang)
    with list_lock:
        idx.append(response_id)
        translation.append(trans)


def main():
    # Main execution
    list_lock = threading.Lock()
    idx = []
    translation = []
    i = 0
    with ThreadPoolExecutor(max_workers=10) as executor:
        for i in range(len(df)):
            executor.submit(process_move, df, i, list_lock, idx, translation)
    df_new = pd.DataFrame({"response_id": idx, "translated_response": translation})
    insert_data(
        df_new,
        "bi_stage_dev_dbo.qualtrics_translations",
        ["response_id", "translated_response"],
    )
    get_logger().info("Done")


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()