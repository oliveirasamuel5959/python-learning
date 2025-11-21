from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from account_api.core.security import oauth2_scheme
from account_api.core.database import get_session
from account_api.api.users.schemas import ClientOut
from account_api.api.users.models import ClientModel
from account_api.core.configs.logger_handler import logger
from account_api.core.auth import get_current_user
from account_api.core.configs.logger_handler import logger

router = APIRouter()

@router.get(
    "/",
    summary="Listar todos os clientes",
    status_code=status.HTTP_200_OK, 
    response_model=list[ClientOut]
)
def get_clients(
    limit: int,
    user: ClientModel = Depends(get_current_user),
    db_session: Session = Depends(get_session),
    ) -> list[ClientOut]:

    logger.info(f"Fetching clients with limit: {limit}")
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

