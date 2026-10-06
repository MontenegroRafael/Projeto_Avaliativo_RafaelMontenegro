import opendatasets as od

# Cole o link da página do dataset do Kaggle
dataset_url = 'https://www.kaggle.com/datasets/faresashraf1001/supermarket-sales'

# Baixa o dataset diretamente na pasta raiz (diretório atual ".")
od.download(dataset_url, data_dir='.')