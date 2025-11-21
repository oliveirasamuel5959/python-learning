from typing import Union, Any
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from jose import jwt
from jose.exceptions import JWTError, ExpiredSignatureError
from pydantic import ValidationError

from account_api.core.configs.logger_handler import logger
from account_api.api.users.models import ClientModel
from account_api.api.auth.schemas import TokenPayload
from account_api.core.database import get_session
from account_api.core.security import ALGORITHM, JWT_SECRET_KEY


reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl="/login",
    scheme_name="JWT"
)


def decode_token(token: str) -> TokenPayload:
    logger.info("Decoding token.")
    logger.debug(f"Raw token: {token}")

    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        logger.debug(f"JWT decode produced payload: {payload}")

        token_data = TokenPayload(**payload)  # pode lançar ValidationError
        return token_data

    except ExpiredSignatureError as exc:
        logger.warning("Token expired.", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except ValidationError as exc:
        # payload não tem a forma que TokenPayload espera
        logger.warning("Token payload validation failed.", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido: payload inválido",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except JWTError as exc:
        # captura erros gerais do python-jose (assinatura inválida, formato, etc)
        logger.warning("JWT error while decoding token.", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except Exception as exc:
        # catch-all - apenas para garantir que sempre logamos o erro
        logger.exception("Erro inesperado ao decodificar token.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro interno ao processar token",
        )


def get_current_user(
    token: str = Depends(reuseable_oauth),
    db: Session = Depends(get_session),
) -> ClientModel:
    logger.info("Getting current user from token.")
    payload = decode_token(token)
    logger.info(f"Decoded token payload: {payload!r}")

    # Verifique que TokenPayload tem atributo 'sub'
    sub = getattr(payload, "sub", None)
    if not sub:
        logger.warning("Token missing 'sub' claim.")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido: 'sub' ausente",
            headers={"WWW-Authenticate": "Bearer"},
        )

    logger.debug(f"Looking up user by email: {sub}")
    user: Union[ClientModel, None] = db.query(ClientModel).filter(ClientModel.email == sub).first()
    if not user:
        logger.warning("User not found for token subject.", extra={"sub": sub})
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário não encontrado",
            headers={"WWW-Authenticate": "Bearer"},
        )

    logger.info(f"Authenticated user id={getattr(user, 'id', 'unknown')} email={getattr(user, 'email', 'unknown')}")
    return user
