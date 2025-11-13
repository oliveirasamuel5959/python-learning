from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from account_api.core.database import SessionLocal
from account_api.client.schemas import ClientIn, ClientOut
from account_api.client.models import ClientModel

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
    summary="Criar um novo cliente",
    status_code=status.HTTP_201_CREATED, 
    response_model=ClientOut
)
async def create_account(account_in: ClientIn, db_session: Session = Depends(get_db)) -> ClientOut:
    client = ClientModel(**account_in.model_dump())
    db_session.add(client)
    db_session.commit()
    return client

@router.get(
    "/",
    summary="Listar todos os clientes",
    status_code=status.HTTP_200_OK, 
    response_model=list[ClientOut]
)
async def get_clients(limit: int, db_session: Session = Depends(get_db)) -> list[ClientOut]:

    query = select(ClientModel).limit(limit)
    clients: list[ClientOut] = db_session.execute(query).scalars().all()

    return clients

@router.get(
    "/{id}",
    summary="Retornar client por id",
    status_code=status.HTTP_200_OK, 
    response_model=ClientOut
)
async def get_client(id: int, db_session: Session = Depends(get_db)) -> ClientOut:

    query = select(ClientModel).where(ClientModel.id == id)
    client: ClientOut = db_session.execute(query).scalars().first()

    if not client:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Client {id} nao foi encontrado."
        )

    return client

@router.delete(
    "/{id}",
    summary="Deletar client por id",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_client(id: int, db_session: Session = Depends(get_db)) -> None:

    query = select(ClientModel).where(ClientModel.id == id)
    client: ClientOut = db_session.execute(query).scalars().first()

    if not client:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Client {id} nao foi encontrado."
        )
    
    db_session.delete(client)
    db_session.commit()

