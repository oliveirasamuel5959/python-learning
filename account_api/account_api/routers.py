from fastapi import APIRouter
from account_api.api.accounts.controller import router as account
from account_api.api.users.controller import router as client
from account_api.api.transactions.controller import router as transaction
from account_api.api.auth.controller import router as auth

api_router = APIRouter()
api_router.include_router(account, prefix='/accounts', tags=['account'])
api_router.include_router(client, prefix='/clients', tags=['client'])
api_router.include_router(transaction, prefix='/transactions', tags=['transaction'])
api_router.include_router(auth, prefix='/auth', tags=['auth'])
