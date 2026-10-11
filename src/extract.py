import pandas as pd
from sqlalchemy import text
from database import engine_projeto
import psycopg2

def extract_base_raw():

    RAW_DIR = "data/raw"

    caminho_csv = f"{RAW_DIR}/Supermarket_Analysis.csv"

    df_supermarket_raw = pd.read_csv(
        caminho_csv,
        sep=",", # Delimitador de campo no arquivo CSV
        encoding="utf-8-sig"
    )

    df_supermarket_raw.to_sql(
        "raw_supermarket", # Nome da tabela no banco de dados
        con=engine_projeto,
        schema="public",
        if_exists="replace", # Substitui os dados existentes
        index=False # Não inclui o índice como uma coluna
    )

    print("Dados gravados em public.raw_supermarket.")