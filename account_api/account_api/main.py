from fastapi import FastAPI
from account_api.routers import api_router


servers = [
        {"url": "http://localhost:8000", "description": "Staging environment"},
        {"url": "https://prod.example.com", "description": "Production environment"},
    ]

app = FastAPI(
    title="Account API",
    version="1.0.0",
    summary="API para controle de transações bancárias",
    description="""
Controle de transferência entre contas bancárias de clientes.

## Posts

You will be able to
* **Criar uma nova conta**.
* **Efetuar saques**.
* **Realizar depositos**.
* **Consultar histórico de transações**.
* **Excluir conta**.
* **Limitar o valor de saque/depósito** (_not implemented_).

    """,
    # openapi_url=None, # disable docs
    servers=servers,
)

app.include_router(api_router)
