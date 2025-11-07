from pydantic import BaseModel, Field
from typing import Annotated, Optional

class DepositoIn(BaseModel):
    bank_name: Annotated[str, Field(description="Nome do banco cadastrado", max_length=50, nullable=False)]
    agencia: Annotated[int, Field(description="Número da agência", gt=0, nullable=False)]
    account_type: Annotated[str, Field(description="Tipo de conta", max_length=20, nullable=False)]

class DepositoOut(DepositoIn):    
    pass
