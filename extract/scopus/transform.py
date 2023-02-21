import pandas as pd
from datetime import date

import sys
from pathlib import Path
sys.path.append(f"{Path().resolve()}/app/")

from settings import RAW_DIR

def transform():
    RAW_DIR
    df = pd.read_parquet('scopus_authors.parquet.gzip', engine='pyarrow')


if __name__ == "__main__":
    transform()
