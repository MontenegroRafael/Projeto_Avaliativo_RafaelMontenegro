import pandas as pd
from sqlalchemy import text
from database import engine_projeto


def transform():
 

    # Leitura das tabelas da camada raw no banco Projeto Avaliativo
    df_vendas = pd.read_sql(
        "SELECT * FROM public.raw_supermarket",
        con=engine_projeto
    )

    print("Dados raw carregados para transformação.")

    # Transformação dos dados

    df_vendas_tratadas = df_vendas.copy()

    # tratando os nomes das colunas, removendo espaços em branco, convertendo para minúsculas e substituindo espaços por underscores
    df_vendas_tratadas.columns = (
        df_vendas_tratadas.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )


    df_vendas_tratadas["date"] = pd.to_datetime(
        df_vendas_tratadas["date"]
    )
    df_vendas_tratadas["date"] = pd.to_datetime(
        df_vendas_tratadas["date"], format="%d/%m/%Y"
    )
   

    # Estatísticas dos produtos
    df_estatisticas = pd.DataFrame({
        "indicador": [
            "quantidade_vendas_produtos",
            "preco_medio",
            "tipo_pagamento",
            "margem_media",
            "quantidade_media_vendas"
        ],
        "valor": [
            df_vendas_tratadas["product_line"].nunique(),
            df_vendas_tratadas["unit_price"].mean(),
            df_vendas_tratadas["payment"].nunique(),
            df_vendas_tratadas["gross_margin_percentage"].mean(),
            df_vendas_tratadas["quantity"].mean()
        ],
    })

    return df_estatisticas, df_vendas_tratadas