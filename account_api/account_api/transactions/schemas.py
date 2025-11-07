from pydantic import BaseModel, Field
from typing import Annotated, Optional

class TransactionIn(BaseModel):
    type: Annotated[str, Field(description="Tipo de transação", max_length=20, nullable=False)]
    value: Annotated[int, Field(description="Valor da transação", gt=0, nullable=False)]

class TransactionOut(TransactionIn):    
    pass
