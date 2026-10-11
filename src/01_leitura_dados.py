import pandas as pd


"""
==================  > RESULTADO DA LEITURA DO DATASET <  ==================

NOMES DAS COLUNAS DO DATASET:
'Invoice ID,
Branch,City,
Customer type,
Gender,
Product line,
Unit price,
Quantity,
Tax 5%,
Sales,
Date,
Time,
Payment,
cogs,
gross margin percentage,
gross income,
Rating'

O dataset possui 1000 linhas e 17 colunas.
NÃO POSSUI VALORES AUSENTES.

 #   Column                   Non-Null Count  Dtype  
---  ------                   --------------  -----  
 0   Invoice ID               1000 non-null   object 
 1   Branch                   1000 non-null   object 
 2   City                     1000 non-null   object 
 3   Customer type            1000 non-null   object 
 4   Gender                   1000 non-null   object 
 5   Product line             1000 non-null   object 
 6   Unit price               1000 non-null   float64
 7   Quantity                 1000 non-null   int64  
 8   Tax 5%                   1000 non-null   float64
 9   Sales                    1000 non-null   float64
 10  Date                     1000 non-null   object 
 11  Time                     1000 non-null   object 
 12  Payment                  1000 non-null   object 
 13  cogs                     1000 non-null   float64
 14  gross margin percentage  1000 non-null   float64
 15  gross income             1000 non-null   float64
 16  Rating                   1000 non-null   float64
dtypes: float64(7), int64(1), object(9)
memory usage: 132.9+ KB

"""

# CARREGA O DATASET EM UM DATAFRAME DO PANDAS
df_leitura_inicial = pd.read_csv(
    'data/raw/Supermarket_Analysis.csv',
    sep=',',
    encoding='utf-8'
    )

# Verificar o tamanho do arquivo
print(f"O dataset possui {df_leitura_inicial.shape[0]} linhas e {df_leitura_inicial.shape[1]} colunas.\n")
    
# Analisar tipos de dados e nulos
print("\n--- Informações Gerais ---")
df_leitura_inicial.info()

# Checar a quantidade de dados faltando
print("\n--- Valores Ausentes por Coluna ---")
print(df_leitura_inicial.isnull().sum())

print(df_leitura_inicial.head()) #Exibe as 5 primeiras linhas
print(df_leitura_inicial.tail()) #Exibe as 5 últimas linhas
print(df_leitura_inicial.columns) #Exibe os nomes das colunas do DataFrame
print(df_leitura_inicial.describe()) #Exibe estatísticas descritivas das colunas numéricas do DataFrame