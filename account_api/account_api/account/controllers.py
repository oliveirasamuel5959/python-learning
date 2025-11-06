from fastapi import APIRouter, Depends
from typing import Annotated
from account_api.account.models import AccountModel
from account_api.account.schemas import AccountIn
from account_api.account.schemas import AccountOut
from sqlalchemy.orm import Session
from account_api.configs.database import SessionLocal, engine, Base

router = APIRouter()

# Create tables in the database
Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
async def create_account(account_in: AccountIn, db_session: Session = Depends(get_db)) -> AccountOut:
    new_account = AccountModel(**account_in.model_dump())
    db_session.add(new_account)
    db_session.commit()
    return new_account

