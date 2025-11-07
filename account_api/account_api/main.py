from fastapi import FastAPI
from account_api.routers import api_router

app = FastAPI(title="Account API")
app.include_router(api_router)
