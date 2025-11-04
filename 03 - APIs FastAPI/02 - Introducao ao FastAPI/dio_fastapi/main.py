
from fastapi import FastAPI
from controllers import post
from controllers.auth import auth
from contextlib import asynccontextmanager
from database import database, engine, metadata

@asynccontextmanager
async def lifespan(app: FastAPI):
    from models.post import posts

    await database.connect()
    metadata.create_all(engine)
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)
app.include_router(post.router)
# app.include_router(auth.router)

