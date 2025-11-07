from fastapi import APIRouter, Depends, HTTPException, status
from account_api.account.models import AccountModel
from account_api.account.schemas import AccountIn
from account_api.account.schemas import AccountOut
from sqlalchemy.orm import Session
from account_api.configs.database import SessionLocal
from sqlalchemy import select

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
    new_account = AccountModel(**account_in.model_dump())
    db_session.add(new_account)
    db_session.commit()
    return new_account

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

