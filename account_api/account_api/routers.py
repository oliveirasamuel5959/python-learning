from fastapi import APIRouter
from account_api.account.controllers import router as account

api_router = APIRouter()
api_router.include_router(account, prefix='/account', tags=['account'])