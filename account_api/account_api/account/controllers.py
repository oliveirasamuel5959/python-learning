from fastapi import APIRouter, Depends
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from account_api.account.models import AccountModel
from account_api.account.schemas import AccountIn
from account_api.account.schemas import AccountOut
from account_api.configs.database import get_session

router = APIRouter()

DatabaseDependency = Annotated[AsyncSession, Depends(get_session)]

@router.post("/")
async def create_account(account_in: AccountIn, db_session: DatabaseDependency) -> AccountOut:

    new_account = AccountModel(**account_in.model_dump())
    db_session.add(new_account)
    db_session.commit()
    return new_account