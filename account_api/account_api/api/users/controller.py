from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from account_api.core.security import oauth2_scheme
from account_api.core.database import get_session
from account_api.api.users.schemas import ClientIn, ClientOut
from account_api.api.users.models import ClientModel
from account_api.core.security import get_password_hash
from account_api.core.configs.logger_handler import logger

router = APIRouter()

@router.post(
    "/",
    summary="Criar um novo cliente",
    status_code=status.HTTP_201_CREATED, 
    # response_model=ClientOut
)
async def create_user(client_in: ClientIn, db_session: Session = Depends(get_session)):

    hash_pwd = get_password_hash(client_in.hash_password)
    
    client_out = ClientIn(
        hash_password=hash_pwd,
        **client_in.model_dump(exclude={"hash_password"})
    )

    client = ClientModel(**client_out.model_dump())

    db_session.add(client)
    db_session.commit()
    db_session.refresh(client)

    return client

@router.get(
    "/",
    summary="Listar todos os clientes",
    status_code=status.HTTP_200_OK, 
    response_model=list[ClientOut]
)
async def get_clients(
    limit: int, 
    db_session: Session = Depends(get_session),
    ) -> list[ClientOut]:

    query = select(ClientModel).limit(limit)
    clients: list[ClientOut] = db_session.execute(query).scalars().all()

    return clients

@router.get(
    "/{id}",
    summary="Retornar client por id",
    status_code=status.HTTP_200_OK, 
    response_model=ClientOut
)
async def get_client(id: int, db_session: Session = Depends(get_session)) -> ClientOut:

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
async def delete_client(id: int, db_session: Session = Depends(get_session)) -> None:

    query = select(ClientModel).where(ClientModel.id == id)
    client: ClientOut = db_session.execute(query).scalars().first()

    if not client:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Client {id} nao foi encontrado."
        )
    
    db_session.delete(client)
    db_session.commit()

