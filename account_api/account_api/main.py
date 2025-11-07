from fastapi import FastAPI
from account_api.routers import api_router

app = FastAPI(
    title="Account API",
    version="1.0.0",
    summary="API para controle de transações bancárias",
)
app.include_router(api_router)
