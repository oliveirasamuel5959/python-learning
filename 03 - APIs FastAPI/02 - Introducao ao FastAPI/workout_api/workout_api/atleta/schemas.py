from pydantic import BaseModel, Field, PositiveFloat
from typing import Annotated

from workout_api.contrib.schemas import BaseSchema

class Atleta(BaseSchema):
    id: int
    nome: Annotated[str, Field(description="Nome completo do atleta", example=["João Silva", "Maria Oliveira"], max_length=50)]
    cpf: Annotated[str, Field(description="Número do CPF do atleta", example=["123.456.789-00", "987.654.321-00"], max_length=11)]
    idade: Annotated[int, Field(description="Idade do atleta", ge=0)]
    peso: Annotated[PositiveFloat, Field(description="Peso do atleta em kg", gt=0, example=[70.5, 82.3])]
    altura: Annotated[PositiveFloat, Field(description="Altura do atleta em metros", gt=0, example=[1.75, 1.80])]
    sexo: Annotated[str, Field(description="Sexo do atleta", example=["M", "F"], max_length=1)]
    