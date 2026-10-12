-- Execute este script manualmente no PostgreSQL.

CREATE TABLE supermarket_raw (
    invoice_id VARCHAR(50) PRIMARY KEY,
    branch VARCHAR(10) NOT NULL,
    city VARCHAR(100) NOT NULL,
    customer_type VARCHAR(50) NOT NULL,
    gender VARCHAR(20),
    product_line VARCHAR(100) NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    quantity INT NOT NULL,
    tax_5porcent DECIMAL(10, 4) NOT NULL,
    sales DECIMAL(10, 2) NOT NULL,
    date_sale DATE NOT NULL,
    time_sale TIME NOT NULL,
    payment VARCHAR(50) NOT NULL,
    cogs DECIMAL(10, 2) NOT NULL,
    gross_margin_percentage DECIMAL(5, 2) NOT NULL,
    gross_income DECIMAL(50, 2) NOT NULL,
    rating DECIMAL(50, 1)
);

CREATE TABLE processed_supermarket (
    id_venda VARCHAR(50) PRIMARY KEY,
    filial VARCHAR(10) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    tipo_cliente VARCHAR(50) NOT NULL,
    genero VARCHAR(20),
    linha_produto VARCHAR(150) NOT NULL,
    preco_unitario NUMERIC(10, 2) CHECK (preco_unitario >= 0),
    quantidade INTEGER CHECK (quantidade > 0),
    imposto NUMERIC(10, 2) CHECK (imposto >= 0),
    valor_total NUMERIC(12, 2) CHECK (valor_total >= 0) NOT NULL,
    data_venda DATE NOT NULL,
    hora_venda TIME NOT NULL,
    forma_pagamento VARCHAR(50) NOT NULL,
    custo_mercadoria NUMERIC(12, 2) CHECK (custo_mercadoria >= 0),
    margem_percentual NUMERIC(10, 2),
    receita_bruta NUMERIC(12, 2) CHECK (receita_bruta >= 0),
    avaliacao NUMERIC(4, 2) CHECK (avaliacao >= 0 AND avaliacao <= 10) 
);