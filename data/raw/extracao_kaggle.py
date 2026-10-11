import opendatasets as od

# Link da página do dataset do Kaggle
dataset_url = 'https://www.kaggle.com/datasets/faresashraf1001/supermarket-sales'

# Baixa o dataset diretamente na pasta raiz através do link fornecido
od.download(dataset_url, data_dir='.')

# Vai precisar inserir suas credencias do Kaggle.