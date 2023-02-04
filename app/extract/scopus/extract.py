import pandas as pd
import pybliometrics
from datetime import date
import os
from os import path
import sys
from pathlib import Path

sys.path.append(f"{Path().resolve()}/app/")

from settings import CONFIG_DIR, SCOPUS_SECRET_KEY, RAW_DIR

from pybliometrics.scopus import AuthorSearch

def config():
    os.environ['PYB_CONFIG_FILE'] = f"{CONFIG_DIR}/scopus_config.ini"
    if (not path.exists(os.environ['PYB_CONFIG_FILE'])):
        # TODO no esta creando el archivo de configuración en la carpeta indicada, sino en ~/.pybliometrics/config.ini
        pybliometrics.scopus.utils.create_config(keys=[SCOPUS_SECRET_KEY])

def extract():
    author_search = AuthorSearch('AF-ID(60032057)')
    pd.set_option('display.max_columns', None)
    df = pd.DataFrame(author_search.authors)
    df.to_parquet(f'{RAW_DIR}/scopus_authors_{date.today()}.parquet.gzip', compression='gzip')  

if __name__ == "__main__":
    config()
    extract()
