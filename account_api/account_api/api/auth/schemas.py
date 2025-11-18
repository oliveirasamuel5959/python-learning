from typing import Annotated
from pydantic import BaseModel, EmailStr, Field

class LoginIn(BaseModel):
    email: Annotated[EmailStr, Field(description="Email do cliente", max_length=50, nullable=False)]
    password: Annotated[str, Field(description="Senha de acesso", max_length=100, nullable=False)]

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None