import pandas as pd
from sqlalchemy import text
import psycopg2
from database import engine_projeto


def load(
    df_estatisticas,
    df_vendas_tratadas
):

    # Gravar tabela estatisticas_produtos
    df_estatisticas.to_sql(
        "estatisticas_produtos",
        con=engine_projeto,
        schema="public",
        if_exists="replace",
        index=False
    )

    print("Tabelas processadas carregadas no PostgreSQL.")

    # Exportar para CSV
    PROCESSED_DIR = "data/processed"

    caminho_csv = f"{PROCESSED_DIR}/vendas_tratadas.csv"

    df_vendas_tratadas.to_csv(
        caminho_csv,
        index=False
    )

    print(f"CSV gerado: {caminho_csv}")


    PROCESSED_DIR_tratado = "data/processed" # Diretório onde o arquivo CSV tratado será salvo

    caminho_csv_tratado = f"{PROCESSED_DIR}/vendas_tratadas.csv" 

    df_vendas_tratadas = pd.read_csv(
        caminho_csv_tratado,
        sep=",", # Delimitador de campo no arquivo CSV
        encoding="utf-8-sig"
    )

    df_vendas_tratadas.to_sql(
        "processed_supermarket", # Nome da tabela no banco de dados
        con=engine_projeto,
        schema="public",
        if_exists="replace", # Substitui os dados existentes
        index=False # Não inclui o índice como uma coluna
    )

    print("Dados gravados em public.processed_supermarket.")
  