from transform import transform
from load import load
from extract import extract_base_raw

# executar todas as etapas do ETL
def run_etl():

    # Extract
    extract_base_raw()

     # Transform
    df_vendas_tratadas, df_estatisticas = transform()
    
    # Load
    load(
        df_vendas_tratadas,
        df_estatisticas
    )

if __name__ == "__main__":
    run_etl()