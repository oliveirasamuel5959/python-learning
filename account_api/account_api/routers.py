from fastapi import APIRouter
from account_api.account.controllers import router as account
from account_api.client.controllers import router as client
from account_api.transactions.controllers import router as transaction

api_router = APIRouter()
api_router.include_router(account, prefix='/account', tags=['accounts'])
api_router.include_router(client, prefix='/client', tags=['clients'])
api_router.include_router(transaction, prefix='/transaction', tags=['transactions'])
