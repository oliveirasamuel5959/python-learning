from pydantic import BaseModel, Field, PositiveFloat
from typing import Annotated

class Atleta(BaseModel):
    id: int
    nome: Annotated[str, Field(description="Nome completo do atleta", examples=["João Silva", "Maria Oliveira"], max_length=50)]
    cpf: Annotated[str, Field(description="Número do CPF do atleta", examples=["123.456.789-00", "987.654.321-00"], max_length=11)]
    idade: Annotated[int, Field(description="Idade do atleta", ge=0)]
    peso: Annotated[PositiveFloat, Field(description="Peso do atleta em kg", gt=0, examples=[70.5, 82.3])]
    altura: Annotated[PositiveFloat, Field(description="Altura do atleta em metros", gt=0, examples=[1.75, 1.80])]
    sexo: Annotated[str, Field(description="Sexo do atleta", examples=["M", "F"], max_length=1)]
    