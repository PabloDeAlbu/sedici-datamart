from decouple import config
import pandas as pd
from datetime import date
import pdb

filepath = config('filepath')
STAGING_DIR = config('STAGING_DIR')

df = pd.read_csv(filepath_or_buffer=filepath, sep=";")

df['es_doble_dependencia'] = df['es_doble_dependencia'].replace('N', 'S') 

df.to_parquet(f'{STAGING_DIR}/scopus_authors_{date.today()}.parquet.gzip', compression='gzip')
