import pandas as pd

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