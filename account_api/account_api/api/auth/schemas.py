from typing import Annotated
from pydantic import BaseModel, EmailStr, Field

class SignupIn(BaseModel):
    email: Annotated[EmailStr, Field(description="Email do cliente", max_length=50, nullable=False)]
    password: Annotated[str, Field(description="Senha de acesso", max_length=100, nullable=False)]

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

class TokenPayload(BaseModel):
    sub: str = None
    exp: int = None
    