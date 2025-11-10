from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select


from datetime import datetime, timezone
from uuid import uuid4

from account_api.configs.database import SessionLocal
from account_api.transactions.schemas import TransactionIn, TransactionOut
from account_api.transactions.models import TransactionModel
from account_api.client.models import ClientModel
from account_api.client.schemas import ClientIn, ClientOut


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
async def transaction(transaction_in: TransactionIn, db_session: Session = Depends(get_db)):

    client_name = transaction_in.client.name
    
    query = select(ClientModel).where(ClientModel.name == client_name)
    client = db_session.execute(query).scalars().first()

    if client is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Client {client_name} nao foi encontrado."
        )
    
    transaction_out = TransactionOut(
        created_at=datetime.now(timezone.utc).replace(tzinfo=None), 
        **transaction_in.model_dump()
    )
    
    transaction_model = TransactionModel(**transaction_out.model_dump(exclude={'client'}))
    transaction_model.client_id = client.id
    
    db_session.add(transaction_model)
    db_session.commit()
    
    return transaction_out
