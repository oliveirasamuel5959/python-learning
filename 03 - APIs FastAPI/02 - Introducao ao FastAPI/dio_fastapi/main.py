from fastapi import FastAPI
from controllers import post
from controllers.auth import auth
from contextlib import asynccontextmanager
from database import database, engine, metadata

servers = [
        {"url": "http://localhost:8000", "description": "Staging environment"},
        {"url": "https://prod.example.com", "description": "Production environment"},
    ]

@asynccontextmanager
async def lifespan(app: FastAPI):
    from models.post import posts

    await database.connect()
    metadata.create_all(engine)
    yield
    await database.disconnect()

app = FastAPI(
    title="Dio blog API",
    version="1.2.0",
    summary="API para blog pessoal",
    description="""
DIO blog API ajuda você a criar seu blog pessoal.

## Posts

You will be able to
* **Criar posts**.
* **Recuperar posts**.
* **Recuperar posts por id**.
* **Atualizar posts**.
* **Excluir posts**.
* **Limitar quantidade de posts diários** (_not implemented_).

    """,
    # openapi_url=None, # disable docs
    servers=servers,
    lifespan=lifespan
)


app.include_router(post.router, tags=["Main"])
# app.include_router(auth.router)

