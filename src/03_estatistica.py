import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_vendas_tratadas = pd.read_csv("data/processed/vendas_tratadas.csv")

print("\nNúmero total de compras por gênero do cliente:")
tabela_produto_por_genero = pd.pivot_table(
    df_vendas_tratadas,
    index="linha_produto",
    columns="genero",
    values="id_venda" if "id_venda" in df_vendas_tratadas.columns else "linha_produto",
    aggfunc="count",
    fill_value=0
)
print(tabela_produto_por_genero)