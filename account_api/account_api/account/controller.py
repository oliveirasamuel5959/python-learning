from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from account_api.account.models import AccountModel
from account_api.account.schemas import AccountIn
from account_api.account.schemas import AccountOut
from account_api.client.models import ClientModel
from account_api.client.schemas import ClientIn
from account_api.client.schemas import ClientOut
from account_api.configs.database import SessionLocal


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
    summary="Criar uma nova conta",
    status_code=status.HTTP_201_CREATED, 
    response_model=AccountOut
)
async def create_account(account_in: AccountIn, db_session: Session = Depends(get_db)) -> AccountOut:

    client_name = account_in.client_name
    agencia = account_in.agencia

    # query_account = select(AccountModel).where(AccountModel.agencia == agencia)
    # account = db_session.execute(query_account).scalars().first()

    query_client = select(ClientModel).where(ClientModel.name == client_name)
    client = db_session.execute(query_client).scalars().first()

    if client is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Client {client_name} nao foi encontrado."
        )
    
    accout_out = AccountOut(
        **account_in.model_dump()
    )

    account_model = AccountModel(**accout_out.model_dump(exclude={"client", "client_name"}))
    account_model.value = 0
    account_model.client_id = client.id
    
    db_session.add(account_model)
    db_session.commit()
    
    return accout_out

@router.get(
    "/",
    summary="Listar todas as contas",
    status_code=status.HTTP_200_OK, 
    # response_model=list[AccountOut]
)
async def get_accounts(db_session: Session = Depends(get_db)):

    query = select(AccountModel)
    results: list[AccountOut] = db_session.execute(query).scalars().all()

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
async def get_account(id: int, db_session: Session = Depends(get_db)) -> AccountOut:

    query = select(AccountModel).where(AccountModel.id == id)
    account: AccountOut = db_session.execute(query).scalars().first()

    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Conta não encontrada no id {id}"
        )

    return account

@router.delete(
    "/{id}",
    summary="Deletar uma conta por ID",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_account(id: int, db_session: Session = Depends(get_db)) -> None:

    query = select(AccountModel).where(AccountModel.id == id)
    result: AccountOut = db_session.execute(query).scalars().first()

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Conta não encontrada no id {id}"
        )

    db_session.delete(result)
    db_session.commit()

