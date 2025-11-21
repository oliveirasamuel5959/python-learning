
from fastapi import FastAPI
from account_api.routers import api_router


servers = [
        {"url": "http://localhost:8000", "description": "Staging environment"},
        {"url": "https://prod.example.com", "description": "Production environment"},
    ]


tags_metadata = [
    {
        "name": "client",
        "description": "Operations to add clients",
    },
    {
        "name": "account",
        "description": "Operations to maintain accounts",
    },
    {
        "name": "transaction",
        "description": "Operations to maintain transactions",
    },
]

app = FastAPI(
    title="Account API",
    version="1.0.0",
    summary="API for banck account transactions control",
    description="""
Banck account transactions management.

## Client

* **Add clients**.
* **List clients**.
* **List client by ID**.
* **Delete client by ID**.

## Account

* **Create accounts**.
* **List accounts**.
* **List account transactions by ID**.
* **Delete account by ID**.

## Transaction

* **Create transactions deposit/withdraw**.
* **Check transactions history by ID**.
* **Limit transactions values* (_not implemented_).

    """,
    openapi_tags=tags_metadata,
    # openapi_url=None, # disable docs
    servers=servers,
)

app.include_router(api_router)
