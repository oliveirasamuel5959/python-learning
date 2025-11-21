from typing import Union, Any
from datetime import datetime
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from account_api.core.configs.logger_handler import logger
from account_api.api.users.models import ClientModel
from account_api.api.auth.schemas import TokenPayload
from account_api.core.database import get_session
from account_api.core.security import ALGORITHM, JWT_SECRET_KEY


from jose import jwt
from pydantic import ValidationError

reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl="/login",
    scheme_name="JWT"
)


def decode_token(token: str) -> dict:
    try:

        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])

        token_data = TokenPayload(**payload)

        return token_data
    
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Token expirado", 
            headers={"WWW-Authenticate": "Bearer"}
        )
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Token inválido", 
            headers={"WWW-Authenticate": "Bearer"}
         )
    
def get_current_user(
    token: str = Depends(reuseable_oauth),
    db: Session = Depends(get_session),
) -> ClientModel:
    
    payload = decode_token(token)

    logger.info(f"Decoded token payload: {payload}")

    if payload.sub is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido: 'sub' ausente",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user: Union[dict[str, Any], None] = db.query(ClientModel).filter(ClientModel.email == payload.sub).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário não encontrado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return user
