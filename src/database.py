import os # Importa o módulo os para acessar variáveis de ambiente
from dotenv import load_dotenv
from sqlalchemy import create_engine # Importa a função create_engine do SQLAlchemy para criar uma conexão com o banco de dados

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env


DATABASE_URL = os.getenv("DATABASE_URL") # Obtém a URL do banco de dados a partir das variáveis de ambiente

engine_projeto = create_engine(DATABASE_URL) # Cria uma engine de conexão com o banco de dados usando a URL obtida