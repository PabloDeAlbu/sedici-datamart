from decouple import AutoConfig
from pathlib import Path
 
ROOT_DIR = f"{Path().resolve()}/app"
HOME_DIR = f"{Path.home()}"
CONFIG_DIR = f"{ROOT_DIR}/config"

config = AutoConfig(search_path=ROOT_DIR)
SCOPUS_SECRET_KEY = config('SCOPUS_SECRET_KEY')
# SCOPUS_CONFIG_DIR = f"{HOME_DIR}/.pybliometrics"

RAW_DIR = f"{Path().resolve()}/data/raw"
PARQUET_DIR = f"{Path().resolve()}/data/parquet"
