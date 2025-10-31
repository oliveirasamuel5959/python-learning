from pydantic import BaseModel, Field, PositiveFloat
from typing import Annotated, Optional

from workout_api.categorias.schemas import CategoriaIn
from workout_api.centro_treinamento.schemas import CentroTreinamentoAtleta
from workout_api.contrib.schemas import BaseSchema, OutMixIn

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description="Nome completo do atleta", example="João Silva", max_length=50)]
    cpf: Annotated[str, Field(description="Número do CPF do atleta", example="123.456.789-00", max_length=20)]
    idade: Annotated[int, Field(description="Idade do atleta", ge=0)]
    peso: Annotated[PositiveFloat, Field(description="Peso do atleta em kg", gt=0, example=70.5)]
    altura: Annotated[PositiveFloat, Field(description="Altura do atleta em metros", gt=0, example=1.80)]
    sexo: Annotated[str, Field(description="Sexo do atleta", example="M", max_length=1)]
    categoria: Annotated[CategoriaIn, Field(description="Categoria do atleta")]
    centro_treinamento: Annotated[CentroTreinamentoAtleta, Field(description="Centro de treinamento do atleta")]
    
class AtletaIn(Atleta):
    pass

class AtletaOut(Atleta, OutMixIn):
    pass

class AtletaUpdate(BaseSchema):
    nome: Annotated[Optional[str], Field(None, description="Nome completo do atleta", example="João Silva", max_length=50)]
    idade: Annotated[Optional[int], Field(None, description="Idade do atleta", example=25, ge=0)]