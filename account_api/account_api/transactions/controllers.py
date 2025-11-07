from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from account_api.configs.database import SessionLocal
from account_api.transactions.schemas import TransactionIn, TransactionOut
from account_api.transactions.models import TransactionModel

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post(
    "/",
    summary="Realizar uma nova transação",
    status_code=status.HTTP_201_CREATED, 
    response_model=TransactionOut
)
async def create_account(transaction_in: TransactionIn, db_session: Session = Depends(get_db)) -> TransactionOut:
    transaction = TransactionModel(**transaction_in.model_dump())
    db_session.add(transaction)
    db_session.commit()
    return transaction
