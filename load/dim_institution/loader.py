from decouple import config
import pandas as pd
from datetime import date
import pdb
import psycopg2
import psycopg2.extras

from sqlalchemy import create_engine

filepath = config('filepath')
STAGING_DIR = config('STAGING_DIR')

DWH_HOST=config('DWH_HOST')
DWH_DB=config('DWH_DB')
DWH_USER=config('DWH_USER')
DWH_PASSWORD=config('DWH_PASSWORD')
DWH_PORT=config('DWH_PORT')
DWH_TABLE = config('DWH_TABLE')

conn = None
cur = None

conn_string = f'postgresql://{DWH_USER}:{DWH_PASSWORD}@{DWH_HOST}:{DWH_PORT}/{DWH_DB}'


df = pd.read_parquet(filepath)

records = []
for index, row in df.iterrows():
    records.append(tuple(row))

try:
    with psycopg2.connect(
                host = DWH_HOST,
                dbname = DWH_DB,
                user = DWH_USER,
                password = DWH_PASSWORD,
                port = DWH_PORT
                ) as conn:

        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:


            cur.fast_executemany = True   # reduce number of calls to server on inserts

            # form SQL statement
            columns = ", ".join(df.columns)
            values = '('+', '.join(['%s']*len(df.columns))+')'
            statement = f"INSERT INTO {DWH_TABLE} ({columns}) VALUES {values}"
            # extract values from DataFrame into list of tuples
            insert = [tuple(x) for x in df.values]

            cur.executemany(statement, insert)


except Exception as error:
    print(error)
finally:
    if conn is not None:
        conn.close()