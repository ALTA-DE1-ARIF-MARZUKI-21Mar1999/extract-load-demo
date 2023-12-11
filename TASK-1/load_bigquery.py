from google.cloud import bigquery
from google.cloud import storage
import os
from io import StringIO
import pandas as pd

def write_to_bigquery(table_id, file_path):
    client = bigquery.Client()
    table = client.get_table(table_id)
    
    if table:
        storage_client = storage.Client()
        bucket_name = 'arifmarzz-alterra-bucket'
        blob = storage_client.bucket(bucket_name).blob(file_path)

        data = blob.download_as_string().decode('utf-8')
        data_io = StringIO(data)
        df = pd.read_json(data_io)

        client.insert_rows_from_dataframe(table, df)

project_id = os.getenv('PROJECT_ID')
table_id = f'{project_id}.my_dataset.my_table2'
file_path = 'arif_task1.json'

write_to_bigquery(table_id, file_path)