from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from account_api.account.models import AccountModel
from account_api.account.schemas import AccountIn
from account_api.account.schemas import AccountOut
from account_api.client.models import ClientModel
from account_api.client.schemas import ClientIn
from account_api.client.schemas import ClientOut
from account_api.core.database import get_session
from account_api.core.auth.auth_bearer import JWTBearer
from account_api.core.auth.auth_handler import decode_jwt


router = APIRouter()

@router.post(
    "/",
    summary="Criar uma nova conta",
    status_code=status.HTTP_201_CREATED, 
    response_model=AccountOut
)
async def create_account(account_in: AccountIn, db_session: Session = Depends(get_session), token: str = Depends(JWTBearer())) -> AccountOut:

    payload = decode_jwt("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiRGFyaXVzLkRhdmlzQHlhaG9vLmNvbSIsImV4cGlyZXMiOjE3NjMwMzc3MjYuMzQxNTA0fQ.1ZF1MmbxpP1Zw5uqV-eIn25GrwfH9ZLmA7mfSAeMets")

    payload = decode_jwt(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    # return payload

    client_name = account_in.client_name
    agencia = account_in.agencia
    
    query_client = select(ClientModel).where(ClientModel.name == client_name)
    client = db_session.execute(query_client).scalars().first()

    if client is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Client {client_name} nao foi encontrado."
        )
    
    accout_out = AccountOut(
        **account_in.model_dump(exclude={"client", "client_name"})
    )

    account_model = AccountModel(**accout_out.model_dump())
    account_model.value = 0
    account_model.client_id = client.id
    
    db_session.add(account_model)
    db_session.commit()
    db_session.refresh(account_model)

    return accout_out

@router.get(
    "/",
    summary="Listar todas as contas",
    status_code=status.HTTP_200_OK, 
    # response_model=list[AccountOut]
)
async def get_accounts(limit: int, db_session: Session = Depends(get_session)):

    query = select(AccountModel).limit(limit)
    results: list[AccountOut] = db_session.execute(query).scalars().all()

    if not results:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nenhuma conta encontrada."
        )

    return {
        "results": results,
        "count": len(results)
    }

@router.get(
    "/{id}",
    summary="Obter detalhes de uma conta por ID",
    status_code=status.HTTP_200_OK, 
    response_model=AccountOut
)
async def get_account(id: int, db_session: Session = Depends(get_session)) -> AccountOut:

    query = select(AccountModel).where(AccountModel.id == id)
    account = db_session.execute(query).scalars().first()

    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Conta não encontrada no id {id}"
        )
    
    account_out = AccountOut(
        bank_name=account.bank_name,
        agencia=account.agencia,
        account_type=account.account_type,
        value=account.value
    )

    return account_out

@router.delete(
    "/{id}",
    summary="Deletar uma conta por ID",
    status_code=status.HTTP_204_NO_CONTENT,
    response_model=None
)
async def delete(id: int, db_session: Session = Depends(get_session)) -> None:

    query = select(AccountModel).where(AccountModel.id == id)
    account = db_session.execute(query).scalars().first()

    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Conta não encontrada no id {id}"
        )

    db_session.delete(account)
    db_session.commit()
    db_session.refresh()

