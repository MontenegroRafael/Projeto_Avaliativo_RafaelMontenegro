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

    colunas_vendas_traducao={
        'Invoice ID': 'id_venda',
        'Branch': 'filial',
        'City': 'cidade',
        'Customer type':
        'tipo_cliente',
        'Gender': 'genero',
        'Product line':
        'linha_produto',
        'Unit price':
        'preco_unitario',
        'Quantity': 'quantidade',
        'Tax 5%': 'imposto',
        'Sales': 'valor_total',
        'Date': 'data_venda',
        'Time': 'hora_venda',
        'Payment': 'forma_pagamento',
        'cogs': 'custo_mercadoria',
        'gross margin percentage': 'margem_percentual',
        'gross income': 'receita_bruta',
        'Rating': 'avaliacao'
        }
    df_vendas_tratadas=df_vendas.rename(columns=colunas_vendas_traducao) #função renomear colunas com base no dicionário criado acima.

    
    # Convertendo as colunas para os tipos correspondentes
    df_vendas_tratadas["data_venda"] = pd.to_datetime(df_vendas_tratadas["data_venda"])

    # tratando os nomes das colunas, removendo espaços em branco, convertendo para minúsculas e substituindo espaços por underscores
    df_vendas_tratadas.columns = (
        df_vendas_tratadas.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    

    # Convertendo a coluna "data_venda" para o formato de data desejado (dd-mm-yyyy)
    df_vendas_tratadas["data_venda"] =  df_vendas_tratadas["data_venda"].dt.strftime("%d-%m-%Y")

    

    

    # Estatísticas dos produtos
    df_estatisticas = pd.DataFrame({
        "indicador": [
            "quantidade_vendas",
            "preco_medio",
            "tipo_pagamento",
            "margem_media"
        ],
        "valor": [
            df_vendas_tratadas["id_venda"].nunique(),
            df_vendas_tratadas["preco_unitario"].mean(),
            df_vendas_tratadas["forma_pagamento"].nunique(),
            df_vendas_tratadas["margem_percentual"].mean()
        ],
    })
    print("Estatisticas geradas.")

    return df_estatisticas, df_vendas_tratadas