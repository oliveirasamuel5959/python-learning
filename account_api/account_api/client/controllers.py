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
