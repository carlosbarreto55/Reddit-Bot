# Reddit Bot

Um bot em Python para buscar e exibir posts do Reddit por palavra-chave, com interface web moderna usando Streamlit.

## 🚀 Funcionalidades

- Busca posts do Reddit por palavra-chave, com opções de limite de resultados, ordenação e filtro de tempo.
- Código organizado com separação clara entre configuração, lógica principal e utilitários.
- Interface web interativa feita com Streamlit: fácil de usar, sem necessidade de programar.
- Pronto para deploy gratuito no [Streamlit Community Cloud](https://streamlit.io/cloud).
- Gerenciamento de ambiente com `venv` e dependências em `requirements.txt`.
- Estrutura preparada para expansão: fácil adicionar cache, logging, banco de dados ou API REST.

## 🛠️ Tecnologias

- Python 3.12+
- Streamlit
- Requests
- python-dotenv
- pytest
- WSL (para desenvolvimento Linux no Windows)

## 📦 Instalação

1. Clone o repositório:
git clone https://github.com/seuusuario/reddit-bot.git
cd reddit-bot


2. Crie e ative um ambiente virtual:
python3 -m venv venv
source venv/bin/activate # No Windows: venv\Scripts\activate


3. Instale as dependências:
pip install -r requirements.txt


## 🚦 Uso

Execute o app Streamlit:
streamlit run app.py

Digite o termo de busca, escolha a quantidade de posts e veja os resultados no navegador.

## 🧩 Estrutura do Projeto

reddit-bot/
├── config.py
├── reddit_searcher.py
├── utils.py
├── app.py
├── requirements.txt
└── README.md

### ⚠️ Important Note on Deployment and Usage ⚠️

Currently, this application is primarily designed for **local execution**. While the project is deployed on Streamlit Community Cloud, you might encounter issues when performing searches directly from the cloud deployment.
