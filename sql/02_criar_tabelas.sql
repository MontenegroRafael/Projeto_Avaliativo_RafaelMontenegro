-- Tabelas de apoio ao projeto ETL TechStore
-- Execute este script manualmente no PostgreSQL.

CREATE TABLE raw_dados_externos (
    id BIGSERIAL PRIMARY KEY, -- id: Um identificador único que cresce automaticamente.
    dados JSONB NOT NULL, -- dados: Onde todo o payload (com colunas desconhecidas) será jogado.
    inserido_em TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP -- inserido_em: Registra exatamente quando o dado bruto chegou.
);


- Registro 1: Tem nome e idade
INSERT INTO raw_dados_externos (dados) 
VALUES ('{"nome": "Lucas", "idade": 28}');

-- Registro 2: Tem colunas totalmente diferentes (empresa, ativo, tags)
INSERT INTO raw_dados_externos (dados) 
VALUES ('{"empresa": "TechCorp", "ativo": true, "tags": ["ti", "cloud"]}');


import pandas as pd
import psycopg2
import json

# 1. Configurações de conexão com o banco de dados
DB_CONFIG = {
    "dbname": "seu_banco",
    "user": "seu_usuario",
    "password": "sua_senha",
    "host": "localhost",
    "port": "5432"
}

CSV_FILE_PATH = "seu_arquivo_desconhecido.csv"

def extrair_e_carregar_raw():
    # 2. Ler o CSV de forma genérica (Pandas detecta as colunas automaticamente)
    # df.to_json(orient="records") transforma cada linha do CSV em um dicionário/JSON
    df = pd.read_csv(CSV_FILE_PATH)
    
    # Preenche valores nulos/vazios para não quebrar o JSON
    df = df.fillna('') 
    
    registros_json = df.to_dict(orient="records")

    # 3. Conectar ao PostgreSQL
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    
    try:
        # 4. Inserção em lote (Bulk Insert) para alta performance
        query = "INSERT INTO raw_dados_externos (dados) VALUES (%s)"
        
        # Transformamos a lista de dicionários Python em strings JSON válidas para o PostgreSQL
        valores_para_inserir = [(json.dumps(registro),) for registro in registros_json]
        
        cursor.executemany(query, valores_para_inserir)
        conn.commit()
        
        print(f"Sucesso! {len(registros_json)} registros inseridos na tabela raw.")
        
    except Exception as e:
        conn.rollback()
        print(f"Erro ao inserir dados: {e}")
        
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    extrair_e_carregar_raw()

    