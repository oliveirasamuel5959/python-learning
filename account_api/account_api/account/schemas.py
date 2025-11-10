from pydantic import BaseModel, Field
from typing import Annotated, Optional
from account_api.client.schemas import ClientIn

class AccountIn(BaseModel):
    bank_name: Annotated[str, Field(description="Nome do banco cadastrado", max_length=50, nullable=False)]
    agencia: Annotated[int, Field(description="Número da agência", gt=0, nullable=False)]
    account_type: Annotated[str, Field(description="Tipo de conta", max_length=20, nullable=False)]
    client_name: Annotated[str, Field(description="Nome do cliente cadastrado", max_length=50, nullable=False)]
    client: Annotated[ClientIn, Field(description="Nome do cliente", nullable=False)]

class AccountOut(AccountIn):    
    pass