-- Execute este script manualmente no PostgreSQL.
-- Query para identificar a quantidade de vendas por filial e o total de vendas em cada filial.
SELECT 
    "Branch" AS NomeFilial, --Transformando o nome da coluna "Branch" para "NomeFilial" para melhor compreensão.
    COUNT(*) AS Quantidade_VendasXFilial, -- Contando as vendas nas filiais e renomeando a coluna para "Quantidade_VendasXFilial".
    SUM("Sales"::numeric) AS TotalVendas
FROM raw_supermarket
GROUP BY "Branch"
ORDER BY TotalVendas DESC; -- Ordenando os resultados pelo total de vendas em ordem decrescente
