# User Management System with FastAPI and Streamlit

## Descrição do Projeto

Este projeto é um sistema de gerenciamento de usuários que utiliza FastAPI para criar uma API RESTful e Streamlit para fornecer uma interface de usuário interativa. O sistema permite realizar operações CRUD (Create, Read, Update, Delete) em um banco de dados SQLite.

## Estrutura do Projeto

```
project/
│
├── main.py                # Arquivo principal para rodar a aplicação FastAPI
├── models.py              # Definição do modelo de dados
├── crud.py                # Operações CRUD
├── controlador.py         # Controle das operações (business logic)
├── banco.db               # Banco de dados SQLite
├── streamlit_app.py       # Interface do usuário com Streamlit
└── README.md              # Documentação do projeto
```


## Requisitos

- Python 3.8 ou superior
- FastAPI
- Uvicorn
- SQLAlchemy
- Streamlit
- Requests

## Instalação

1. **Clone o repositório:**

   ```sh
   git clone https://github.com/marcobarem/FastApi-Streamlit.git
   cd user-management-system

## Instale as dependências:

!pip install fastapi uvicorn sqlalchemy pydantic streamlit requests

## Executando a Aplicação

# Inicie o servidor FastAPI:

    uvicorn main:app --reload

# Inicie a interface Streamlit:

    streamlit run streamlit_app.py
