from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta
from sqlalchemy.orm import Session
from sqlalchemy import select
from account_api.core.database import get_session
from account_api.client.schemas import ClientIn, ClientOut, Token
from account_api.client.models import ClientModel
from account_api.core.security import auth_user, get_password_hash
from account_api.core import security
from account_api.core.security import create_token, get_current_active_user

router = APIRouter()

@router.post(
    "/token",
    summary="Authentication",
    status_code=status.HTTP_200_OK, 
    response_model=Token
)
async def login_for_access_token(client_in: ClientIn, form_data: OAuth2PasswordRequestForm = Depends()):
    user = auth_user(form_data.username, form_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Usuário ou senha inválidos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=security.TOKEN_EXPIRE_MINUTES)
    access_token = create_token(data={"sub": user.name}, expires_delta=access_token_expires)

    return {"access_token": access_token, "token_type": "bearer"}
    

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
    current_user: ClientModel = Depends(get_current_active_user)
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

