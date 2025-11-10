from fastapi import APIRouter
from account_api.account.controller import router as account
from account_api.client.controller import router as client
from account_api.transactions.controller import router as transaction

api_router = APIRouter()
api_router.include_router(account, prefix='/accounts', tags=['accounts'])
api_router.include_router(client, prefix='/clients', tags=['clients'])
api_router.include_router(transaction, prefix='/transactions', tags=['transactions'])
