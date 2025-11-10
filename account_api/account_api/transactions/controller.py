from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select


from datetime import datetime, timezone
from uuid import uuid4

from account_api.configs.database import SessionLocal
from account_api.transactions.schemas import TransactionIn, TransactionOut
from account_api.transactions.models import TransactionModel
from account_api.client.models import ClientModel
from account_api.account.models import AccountModel


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
    
    query_client = select(ClientModel).where(ClientModel.name == client_name)
    client = db_session.execute(query_client).scalars().first()

    if client is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Client {client_name} nao foi encontrado."
        )

    query_account = select(AccountModel).where(AccountModel.client_id == client.id)
    account = db_session.execute(query_account).scalars().first()

    if account is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Conta do client {client_name} nao foi encontrado."
        )
    
    if transaction_in.type == "deposito":
        account.value = account.value + transaction_in.value
        db_session.commit()
        db_session.refresh(account)

    elif transaction_in.type == "saque":
        account.value = account.value - transaction_in.value
        db_session.commit()
        db_session.refresh(account)

    
    transaction_out = TransactionOut(
        created_at=datetime.now(timezone.utc).replace(tzinfo=None), 
        **transaction_in.model_dump()
    )
    
    transaction_model = TransactionModel(**transaction_out.model_dump(exclude={'client'}))
    transaction_model.client_id = client.id
    
    db_session.add(transaction_model)
    db_session.commit()
    
    return transaction_out



@router.get(
    "/",
    summary="Listar todas as transações",
    status_code=status.HTTP_200_OK, 
    # response_model=list[TransactionOut]
)
async def transactions_history(db_session: Session = Depends(get_db)):

    query_transaction = select(TransactionModel)
    transactions: list[TransactionOut] = db_session.execute(query_transaction).scalars().all()

    if not transactions:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nenhuma transação encontrada."
        )
    
    return transactions



@router.get(
    "/{client_id}",
    summary="Listar transações por id",
    status_code=status.HTTP_200_OK, 
    # response_model=list[TransactionOut]
)
async def transactions_history(client_id: int, db_session: Session = Depends(get_db)):

    query_transaction = select(TransactionModel).where(TransactionModel.client_id == client_id)
    transactions: TransactionOut = db_session.execute(query_transaction).scalars().all()

    if not transactions:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Nenhuma transação encontrada para o id {id}."
        )
    
    return transactions


@router.delete(
    "/{client_id}",
    summary="Deletar transações por id",
    status_code=status.HTTP_204_NO_CONTENT, 
    # response_model=list[TransactionOut]
)
async def transactions_history(client_id: int, db_session: Session = Depends(get_db)) -> None:

    query_transaction = select(TransactionModel).where(TransactionModel.client_id == client_id)
    transactions: TransactionOut = db_session.execute(query_transaction).scalars().first()

    if not transactions:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Nenhuma transação encontrada para o id {id}."
        )
    
    db_session.delete(transactions)
    db_session.commit()

