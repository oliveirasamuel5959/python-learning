from pydantic import BaseModel, Field
from typing import Annotated

class AccountIn(BaseModel):
    nome: Annotated[str, Field(description="Nome completo do cliente", example="João Silva", max_length=50)]
    account_type: Annotated[str, Field(description="Tipo de conta", example=["corrent", "poupança"], max_length=50)]
    cpf: Annotated[str, Field(description="Número do CPF do cliente", example="123.456.789-00", max_length=20)]

class AccountOut(AccountIn):
    pass