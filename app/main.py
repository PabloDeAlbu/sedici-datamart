import click
from datetime import date
from scopus import extract as scopus_extract 

import sys
from pathlib import Path
sys.path.append(f"{Path().resolve()}/app/")

from settings import SCOPUS_CONFIG_DIR, SCOPUS_SECRET_KEY

def config():
    print('define your config')

@click.command()
@click.option('--date', default=date.today(), help='Fecha de la corrida')
@click.option('--source', default='example', help='Origen de la extracción')
@click.option('--task', default='example', help='Tarea a ejecutar')
def extract(source, date, task):
    print(source, task)

if __name__ == "__main__":
    extract()
