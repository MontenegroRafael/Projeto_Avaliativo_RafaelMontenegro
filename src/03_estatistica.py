import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Carrega o dataset tratado
df_vendas_tratadas = pd.read_csv("data/processed/vendas_tratadas.csv")

print(df_vendas_tratadas.describe()) #Exibe estatísticas descritivas das colunas numéricas do DataFrame

print("\nNúmero total de compras por gênero do cliente X linha de produto:")

# Cria uma tabela dinâmica para contar o número de compras por gênero do cliente
tabela_produto_por_genero = pd.pivot_table(
    df_vendas_tratadas,
    index="linha_produto", # Agrupa por linha de produto
    columns="genero", # Agrupa por gênero do cliente
    values="id_venda" if "id_venda" in df_vendas_tratadas.columns else "linha_produto",
    aggfunc="count", # Conta o número de vendas
    fill_value=0 # Preenche valores ausentes com 0
)
print(tabela_produto_por_genero)

# >>>>>>>>>>>>>>ANALISE DE VENDAS POR FILIAL<<<<<<<<<<<<<<
# Identifica a filial com maior faturamento.

# Agrupando o faturamento por filial e somando
faturamento_por_filial = (
    df_vendas_tratadas.groupby("filial")["valor_total"].sum().reset_index()
)
# Ordenando do maior para o menor faturamento
faturamento_por_filial = faturamento_por_filial.sort_values(
    by="valor_total", ascending=False
)
# Configurando o estilo do gráfico
plt.figure(figsize=(10, 6)) # Define o tamanho da figura
sns.set_theme(style="whitegrid")
# Criando o gráfico de barras
grafico = sns.barplot(
    x="filial",
    y="valor_total",
    data=faturamento_por_filial,
    palette="Blues_r",  # '_r' inverte a paleta para a maior barra ficar com a cor mais escura
)
# Adicionando rótulos com os valores em cima das barras
for container in grafico.containers:
    grafico.bar_label(container, fmt="R$ %.2f", padding=3)
# Títulos e rótulos dos eixos
plt.title(
    "Filial com Maior Faturamento (Identificação da Maior Unidade)",
    fontsize=14, # Tamanho da fonte do título
    fontweight="bold",
)
plt.xlabel("Filiais", fontsize=12)
plt.ylabel("Faturamento Acumulado (R$)", fontsize=12)

plt.tight_layout() # Ajusta o layout para que os elementos não se sobreponham
plt.show() # Exibindo o gráfico

# >>>>>>>>>>>>>>ANALISE DE VENDAS POR CATEGORIA DE PRODUTO<<<<<<<<<<<<<<
# verifica quai categorias de produtos vendem mais.

# Agrupando os dados por categoria e somando as vendas
vendas_por_categoria = df_vendas_tratadas.groupby("linha_produto")["valor_total"].sum().sort_values(ascending=False)

# Configurando o destaque (explode) para a categoria que mais vendeu
explode = [0.1 if i == 0 else 0 for i in range(len(vendas_por_categoria))] # O primeiro elemento (maior venda) terá um pequeno afastamento de 0.1

# Criando o gráfico de pizza
plt.figure(figsize=(8, 6))
plt.pie(
    vendas_por_categoria,
    labels=vendas_por_categoria.index,
    autopct="%1.1f%%",  # Mostra a porcentagem com uma casa decimal
    startangle=140,  # Rotaciona o gráfico para um melhor ângulo visual
    explode=explode,  # Destaca a maior categoria
    shadow=True,  # Adiciona uma sombra para efeito 3D leve
    colors=["#ff9999", "#66b3ff", "#99ff99", "#ffcc99"],  # Cores personalizadas
)

# Adicionando título e exibindo
plt.title("Proporção de Vendas por Categoria de Produto", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.show()


# >>>>>>>>>>>>>>ANALISE DA FORMA DE PAGAMENTO MAIS UTILIZADA<<<<<<<<<<<<<<
# Conhecer a forma de pagamento mais utulizada pelos clientes.

print("========  Forma de Pagamento Mais Utilizada  ========\n")

tabela_vendas_por_forma_pagamento = pd.pivot_table(
    df_vendas_tratadas,
    index="linha_produto", # Agrupa por forma de pagamento
    columns="forma_pagamento", # Agrupa por forma de pagamento
    values="id_venda" if "id_venda" in df_vendas_tratadas.columns else "forma_pagamento",
    aggfunc="count", # Conta o número de vendas
    fill_value=0 # Preenche valores ausentes com 0
)

# vai gerar um CSV com a tabela de vendas por forma de pagamento, que será salvo no diretório "resultados/estatisticas" com o nome "Forma_pagamento_mais_utilizada.csv"
print(tabela_vendas_por_forma_pagamento)
PROCESSED_DIR = "resultados/estatisticas"

caminho_csv = f"{PROCESSED_DIR}/Forma_pagamento_mais_utilizada.csv"

tabela_vendas_por_forma_pagamento.to_csv(
    caminho_csv,
)

print(f"CSV gerado: Forma_pagamento_mais_utilizada.csv {caminho_csv}")

# >>>>>>>>>>>>>>ANALISE DO VALOR MÉDIO DAS VENDAS<<<<<<<<<<<<<<
# Calcular o valor médio das vendas.

# Calculando a média de vendas por categoria
media_vendas = df_vendas_tratadas.groupby('linha_produto')['preco_unitario'].mean()

# Gerando o gráfico de barras
media_vendas.plot(
    kind='bar', color='skyblue', edgecolor='black', figsize=(8, 5)
)

# Personalizando o gráfico
plt.title('Valor Médio de Vendas por Categoria', fontsize=14)
plt.xlabel('Categoria', fontsize=12)
plt.ylabel('Média de Vendas (R$)', fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Exibindo o gráfico
plt.tight_layout()
plt.show()

# >>>>>>>>>>>>>>ANALISE do DESEMPENHO POR FILIAL: RECEITA VS AVALIAÇÃO<<<<<<<<<<<<<<
# Comparar o desempenho das filiais com base em receita e avaliação.


# Agrupando por Filial e calculando a média das 3 métricas
df_medias = (
    df_vendas_tratadas.groupby("filial")[["valor_total", "receita_bruta", "avaliacao"]].mean().reset_index() 
)

# Transformando o DataFrame para o formato "long" (ideal para o Seaborn)
df_long = pd.melt(
    df_medias,
    id_vars=["filial"],
    value_vars=["valor_total", "receita_bruta", "avaliacao"],
    var_name="Metrica",
    value_name="Valor_Medio",
)

# Configurando e desenhando o gráfico de barras agrupadas
plt.figure(figsize=(10, 6))
sns.barplot(data=df_long, x="filial", y="Valor_Medio", hue="Metrica")

# Customização do gráfico
plt.title("Médias de Faturamento, Avaliação e Lucro por Filial", fontsize=14, pad=15)
plt.xlabel("Filiais", fontsize=12)
plt.ylabel("Valor Médio (R$)", fontsize=12)
plt.legend(title="Médias")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Exibir o gráfico
plt.tight_layout()
plt.show()

# >>>>>>>>>>>>>>ANALISE DO VOLUME DE AVALIAÇÕES POR FILIAL<<<<<<<<<<<<<<
# Agrupando por filial e calculando a média das avaliações
df_agrupado = df_vendas_tratadas.groupby("filial")["avaliacao"].mean().reset_index()

# Criando o gráfico de pizza
plt.figure(figsize=(6, 6))
plt.bar(df_agrupado["filial"], df_agrupado["avaliacao"], color=["#4CAF50", "#2196F3", "#FF9800"])
plt.ylim(0, 10)  # Define o limite do eixo y para melhor visualização

# Customizações finais
plt.title("Proporção da Média de Avaliações por Filial")
plt.tight_layout()

# Exibir o gráfico
plt.show()


# >>>>>>>>>>>>>>ANALISE DE VENDAS POR PERÍODO (MENSAL) - IDENTIFICAÇÃO DE PICO DE VENDAS<<<<<<<<<<<<<<
# Identificar o período de maior volume de vendas, destacando o ponto de pico no gráfico.

# Garante que a coluna de data está no formato correto de datetime
df_vendas_tratadas["data_venda"] = pd.to_datetime(df_vendas_tratadas["data_venda"], format="%d-%m-%Y")

# Agrupa os dados por período (Mensal) e soma a quantidade
# Criamos uma coluna temporária 'Ano_Mes' para o agrupamento gráfico
df_vendas_tratadas["Ano_Mes"] = df_vendas_tratadas["data_venda"].dt.to_period("M").astype(str)
vendas_periodo = (
    df_vendas_tratadas.groupby("Ano_Mes")["quantidade"].sum().reset_index()
)

# Identifica automaticamente o período de maior venda
maior_venda = vendas_periodo.loc[vendas_periodo["quantidade"].idxmax()]

# Configuração e construção do gráfico
plt.figure(figsize=(12, 6))
sns.set_theme(style="whitegrid")

# Desenha a linha de evolução temporal
sns.lineplot(
    data=vendas_periodo,
    x="Ano_Mes",
    y="quantidade",
    marker="o",
    color="#1f77b4",
    linewidth=2.5,
    label="Quantidade Vendida",
)

# Destaca o ponto máximo com uma bola vermelha maior
plt.scatter(
    maior_venda["Ano_Mes"],
    maior_venda["quantidade"],
    color="red",
    s=180,
    zorder=5,
    label=f"Pico de Vendas ({maior_venda['Ano_Mes']})",
)

# Adiciona a seta e o texto apontando para o maior valor
plt.annotate(
    f"Maior Volume: {maior_venda['quantidade']} un.",
    xy=(maior_venda["Ano_Mes"], maior_venda["quantidade"]),
    xytext=(15, 15),
    textcoords="offset points",
    arrowprops=dict(arrowstyle="->", color="red", lw=2),
    color="red",
    weight="bold",
    fontsize=11,
)

# Ajustes de títulos e eixos
plt.title(
    "Evolução de Vendas - Identificação do Maior Período",
    fontsize=16,
    weight="bold",
    pad=15,
)
plt.xlabel("Período (Ano-Mês)", fontsize=12)
plt.ylabel("Total de Itens Vendidos", fontsize=12)
plt.xticks(rotation=45)
plt.legend(loc="upper left")

plt.tight_layout()
plt.show()