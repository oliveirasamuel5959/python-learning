from pydantic import BaseModel, Field
from typing import Annotated, Optional
from account_api.api.users.schemas import ClientIn

class AccountIn(BaseModel):
    bank_name: Annotated[str, Field(description="Nome do banco cadastrado", max_length=50, nullable=False)]
    agencia: Annotated[str, Field(description="Número da agência", nullable=False)]
    account_type: Annotated[str, Field(description="Tipo de conta", max_length=20, nullable=False)]
    client_name: Annotated[str, Field(description="Nome do cliente cadastrado", max_length=50, nullable=False)]
    client: Annotated[ClientIn, Field(description="Nome do cliente", nullable=False)]

class AccountOut(BaseModel):    
    bank_name: Annotated[str, Field(description="Nome do banco cadastrado", max_length=50, nullable=False)]
    agencia: Annotated[str, Field(description="Número da agência", nullable=False)]
    account_type: Annotated[str, Field(description="Tipo de conta", max_length=20, nullable=False)]
    # client_name: Annotated[str, Field(description="Nome do cliente cadastrado", max_length=50, nullable=False)]
    value: Annotated[int, Field(description="Valor na conta", nullable=False)]