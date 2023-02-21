from decouple import config
import pandas as pd
from datetime import date
import pdb

filepath = config('filepath')
STAGING_DIR = config('STAGING_DIR')

df = pd.read_csv(filepath_or_buffer=filepath, sep=";")

df.rename(
    columns={
        'sigla': 'abbreviation',
        'es_doble_dependencia': 'sicytar_es_doble_dependencia',
        'institucion_nivel1_id': 'sicytar_institucion_nivel1_id',
        'institucion_nivel2_id': 'sicytar_institucion_nivel2_id',
        'institucion_nivel3_id': 'sicytar_institucion_nivel3_id',
        'institucion_nivel4_id': 'sicytar_institucion_nivel4_id',
        'institucion_nivel5_id': 'sicytar_institucion_nivel5_id',
        'institucion_nivel6_id': 'sicytar_institucion_nivel6_id',
        'organizacion_id': 'sicytar_organizacion_id',
        'institucion_nivel1_descripcion': 'sicytar_institucion_nivel1_descripcion',
        'institucion_nivel2_descripcion': 'sicytar_institucion_nivel2_descripcion',
        'institucion_nivel3_descripcion': 'sicytar_institucion_nivel3_descripcion',
        'institucion_nivel4_descripcion': 'sicytar_institucion_nivel4_descripcion',
        'institucion_nivel5_descripcion': 'sicytar_institucion_nivel5_descripcion',
        'institucion_nivel6_descripcion': 'sicytar_institucion_nivel6_descripcion',
        'nivel': 'sicytar_nivel'
    },
    inplace=True
)

df = df.drop(['tipo_entidad_privada_id', 'estado_organizacion_id', 'tipo_institucion_id'], axis=1)

int_columns = [
    'sicytar_institucion_nivel1_id', 
    'sicytar_institucion_nivel2_id',
    'sicytar_institucion_nivel3_id', 
    'sicytar_institucion_nivel4_id', 
    'sicytar_institucion_nivel5_id', 
    'sicytar_institucion_nivel6_id', 
    'sicytar_organizacion_id', 
    'sicytar_nivel',
    ]

df[int_columns] = df[int_columns].fillna(0)

str_columns = [
    'abbreviation',
    'sicytar_institucion_nivel1_descripcion',
    'sicytar_institucion_nivel2_descripcion',
    'sicytar_institucion_nivel3_descripcion',
    'sicytar_institucion_nivel4_descripcion',
    'sicytar_institucion_nivel5_descripcion',
    'sicytar_institucion_nivel6_descripcion',
    'sicytar_es_doble_dependencia',
]

df[str_columns] = df[str_columns].fillna('No Informado')

convert_dict = {}

for i in str_columns:
    convert_dict[i] = pd.StringDtype()

for i in int_columns:
    convert_dict[i] = int

df = df.astype(convert_dict)

# El nombre del menor de los hijos será el nombre de la institución
df['name'] = 'No Informado'
for i in range(6, 0 , -1):
    descr_col = f'sicytar_institucion_nivel{i}_descripcion'
    df_n = df[['name', descr_col]]
    df_n.loc[df[descr_col] != "No Informado",'name'] = df_n[descr_col]
     
df['name'] = df_n['name']

parquet_engine = 'pyarrow'
df.to_parquet(f'{STAGING_DIR}/dim_institution.parquet.gzip', engine = parquet_engine, compression='gzip')
