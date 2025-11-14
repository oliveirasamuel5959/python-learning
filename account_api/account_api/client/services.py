from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from account_api.core.database import get_session
from account_api.client.schemas import ClientIn, ClientOut
from account_api.client.models import ClientModel


def get_user(username: str, db_session: Session = Depends(get_session)):

    query = select(ClientModel).where(ClientModel.name == username)
    user = db_session.execute(query).scalars().first()

    if not user:
        return None
    
    return user