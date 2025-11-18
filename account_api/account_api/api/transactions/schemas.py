from pydantic import BaseModel, Field
from datetime import datetime
from typing import Annotated
from account_api.client.schemas import ClientIn

class OutMixIn(BaseModel):
  created_at: Annotated[datetime, Field(description="Data de criação")]

class TransactionIn(BaseModel):
    type: Annotated[str, Field(description="Tipo de transação", max_length=20, nullable=False)]
    value: Annotated[float, Field(description="Valor da transação", gt=0, nullable=False)]
    client: Annotated[ClientIn, Field(description="Nome do cliente", nullable=False)]

class TransactionOut(TransactionIn, OutMixIn):    
    pass

