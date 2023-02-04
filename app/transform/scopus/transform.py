import pandas as pd
from datetime import date

import sys
from pathlib import Path
sys.path.append(f"{Path().resolve()}/app/")

from settings import RAW_DIR

def transform():
    RAW_DIR
    data = (RAW_DIR + '/scopus_authors.parquet.gzip')
    df = pd.read_parquet(data, engine='pyarrow')
    

    breakpoint()

if __name__ == "__main__":
    transform()
