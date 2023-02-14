from decouple import config
from sqlalchemy import create_engine
import pandas as pd
import os

USER = config('USER')
PASSWORD = config('PASSWORD')
SERVER = config('SERVER')
DB_PORT = config('DB_PORT', default=5432, cast=int)
DB_NAME = config('DB_NAME')

def load(df, tbl):
    try:
        rows_imported = 0
        engine = create_engine(f'postgresql://{USER}:{PASSWORD}@{SERVER}:{DB_PORT}/{DB_NAME}')
        print(f'importing rows {rows_imported} to {rows_imported + len(df)}... for table {tbl}')
        df.to_sql(f'stg_{tbl}', engine, if_exists='replace', index=False)
        rows_imported += len(df)
        print("Data imported successful")
    except Exception as e:
        print("Data load error: " + str(e))

