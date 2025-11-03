from sqlalchemy import create_engine
from sqlalchemy import inspect
from models import Base

# conexão com o banco de dados
engine = create_engine("sqlite://")

# criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)

# print(engine.table_names())

inspetor_engine = inspect(engine)
print(inspetor_engine.get_table_names())