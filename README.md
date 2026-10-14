O repositório **Projeto_Avaliativo_RafaelMontenegro**, desenvolvido por **Rafael Montenegro**, é composto por código em **Python** e estruturado para a criação de um pipeline de dados, execução de rotinas em SQL e resolução de perguntas de negócio.

A organização do projeto é composta pelos diretórios `data/`, `sql/`, `src/` e `resultados/`, além dos arquivos `requirements.txt`, `.gitignore` e `README.md`. O histórico de alterações do repositório evidencia etapas de criação de tabelas, carga de arquivos CSV, renomeação de colunas, criação do pipeline e persistência das respostas de negócio. 

```markdown
# Projeto Avaliativo - Rafael Montenegro

Repositório do projeto avaliativo desenvolvido por **Rafael Montenegro**, voltado para a estruturação de um pipeline de dados em **Python**, modelagem e carga de dados via **SQL**, e análise para respostas a perguntas de negócio.

---

## 📁 Estrutura do Repositório

Projeto_Avaliativo_RafaelMontenegro/
│
├── data/              # Armazenamento dos conjuntos de dados e arquivos CSV utilizados
		/processed
        /raw
      
├── sql/               # Scripts SQL (criação de tabelas, carga de CSV e renomeação de colunas)
		/01_criar_banco.sql
        /02_criar-tabelas.sql
├── src/               # Código-fonte em Python (pipeline de processamento e lógica analítica)
		/01_leitura_dados.py
        /02_etl_vendas.py
        /03_estatisticas.py
├── resultados/        # Diretório destinado às respostas e saídas das perguntas de negócio
				/estatisticas
                /graficos
├── .gitignore         # Configurações de exclusão de arquivos do Git
├── requirements.txt   # Dependências e bibliotecas Python do projeto
└── README.md          # Documentação do repositório
```

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** [Python](https://www.python.org/) (100% da base do projeto)
- **Banco de Dados:** SQL (scripts de criação de esquema, carga e ajustes de colunas) Banco de dados PostgreSQL
- **Gerenciamento de Pacotes:** `requirements.txt`
- **Controle de Versão:** Git / GitHub

---

## ⚙️ Fluxo e Arquitetura do Pipeline

1. **Estruturação do Banco e Carga (`sql/`):**

   - Execução de scripts SQL para definição das tabelas.
   - Processamento de carga (*load*) das bases em CSV a partir de `data/`, aplicando renomeação e padronização de colunas.
2. **Pipeline de Dados (`src/`):**

   - Rotinas em Python responsáveis pelo fluxo de ingestão, transformação e processamento dos dados.
3. **Análise de Negócio (`resultados/`):**

   - Execução das rotinas que respondem às perguntas de negócio propostas na avaliação, com salvamento das métricas e conclusões na pasta `resultados/`.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos

- Python instalado
- Banco de dados relacional configurado para execução dos scripts SQL (PostgreSQL))
- Git

### Instruções

1. **Clonar o Repositório:**

   ```bash
   git clone https://github.com/MontenegroRafael/Projeto_Avaliativo_RafaelMontenegro.git
   cd Projeto_Avaliativo_RafaelMontenegro
   ```
2. **Criar e Ativar o Ambiente Virtual:**

   ```bash
   python -m venv venv
   # No Linux/macOS:
   source venv/bin/activate
   # No Windows:
   venv\Scripts\activate
   ```
3. **Instalar Dependências:**

   ```bash
   pip install -r requirements.txt
   ```
4. **Executar Scripts de Banco de Dados:**

   - Execute os arquivos em `sql/` para preparar o banco e carregar os dados de `data/`.
5. **Executar o src:**

   - Execute os scripts contidos em `src/02_etl_vendas.py` para processar os dados e gerar as respostas.
6. **Conferir Resultados:**

   - Os arquivos e relatórios gerados estarão disponíveis no diretório `resultados/` e também executando o `src/03_estatisticas.py` .

---

## 📌 Perguntas de Negócio

<!-- Insira aqui o detalhamento das perguntas de negócio avaliadas e os principais achados -->

- **Pergunta 1:** Qual filial apresentou o maior faturamento?
- **Pergunta 2:** Qual filial realizou a  maoir quantidade de vendas?
- **Pergunta 3:** Qual linha de produto apresentou o maior faturamento?
- **Pergunta 4:** Qual linha de produto recebeu a melhor avaliação média?
- **Pergunta 5:** Qual forma de pagamento mais utilizada?
- **Pergunta 6:** Qual foi o valor médio das vendas?
- **Pergunta 7:** Qual foi a maoir venda registrada?
- **Pergunta 8:** Em que dia da semana ocorreu a maior quantidade de vendas?

---

## 👤 Autor

- **Rafael Montenegro**
  - GitHub: [@MontenegroRafael](https://github.com/MontenegroRafael)
