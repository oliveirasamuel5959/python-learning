from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from account_api.configs.database import SessionLocal
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
async def get_clients(db_session: Session = Depends(get_db)) -> list[ClientOut]:

    query = select(ClientModel)
    clients: list[ClientOut] = db_session.execute(query).scalars().all()

    return clients
