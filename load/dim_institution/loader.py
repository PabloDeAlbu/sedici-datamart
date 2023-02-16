from decouple import config
import pandas as pd
from datetime import date
import pdb

from sqlalchemy import create_engine
import pyodbc

filepath = f"{config('filepath')}_{date.today()}"
STAGING_DIR = config('STAGING_DIR')

DWH_HOST=config('DWH_HOST')
DWH_PORT=config('DWH_PORT')
DWH_DB=config('DWH_DB')
DWH_USER=config('DWH_USER')
DWH_PASSWORD=config('DWH_PASSWORD')

df = pd.read_parquet(filepath)

def load():
    # Create an engine instance
    alchemyEngine = create_engine(f'postgresql://{DWH_USER}:{DWH_PASSWORD}@{DWH_HOST}:{DWH_PORT}/{DWH_DB}')
    
    # Connect to PostgreSQL server
    dbConnection = alchemyEngine.connect()
    
    # Read data from PostgreSQL database table and load into a DataFrame instance
    dataFrame = pd.read_sql("select * from \"general.dim_institution\"", dbConnection)
    
    pd.set_option('display.expand_frame_repr', False)
    
    # Print the DataFrame
    print(dataFrame)
    
    # Close the database connection
    dbConnection.close()
    breakpoint()

#load data to postgres
def load(df, tbl):
    try:
        rows_imported = 0
        engine = create_engine(f'postgresql://{DWH_USER}:{DWH_PASSWORD}@{DWH_HOST}:{DWH_PORT}/{DWH_DB}')
 
        print(f'importing rows {rows_imported} to {rows_imported + len(df)}... ')
        # save df to postgres
        df.to_sql(f"stg_{tbl}", engine, if_exists='replace', index=False)
        rows_imported += len(df)
        # add elapsed time to final print out
        print("Data imported successful")
    except Exception as e:
        print("Data load error: " + str(e))

try:
    load()
except Exception as e:
    print("Data load error: " + str(e))