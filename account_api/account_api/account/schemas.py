from pydantic import BaseModel, Field
from typing import Annotated, Optional

# nome: Annotated[str, Field(description="Nome completo do atleta", example="João Silva", max_length=50)]
# cpf: Annotated[str, Field(description="Número do CPF do atleta", example="123.456.789-00", max_length=20)]
# idade: Annotated[int, Field(description="Idade do atleta", ge=0)]
# peso: Annotated[PositiveFloat, Field(description="Peso do atleta em kg", gt=0, example=70.5)]
# altura: Annotated[PositiveFloat, Field(description="Altura do atleta em metros", gt=0, example=1.80)]
# sexo: Annotated[str, Field(description="Sexo do atleta", example="M", max_length=1)]
# categoria: Annotated[CategoriaIn, Field(description="Categoria do atleta")]
# centro_treinamento: Annotated[CentroTreinamentoAtleta, Field(description="Centro de treinamento do atleta")]

class AccountIn(BaseModel):
    bank_name: Annotated[str, Field(description="Nome do banco cadastrado", max_length=50, nullable=False)]
    agencia: Annotated[int, Field(description="Número da agência", gt=0, nullable=False)]
    account_type: Annotated[str, Field(description="Tipo de conta", max_length=20, nullable=False)]

class AccountOut(AccountIn):    
    pass