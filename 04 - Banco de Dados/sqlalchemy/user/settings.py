from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import inspect
from models import Base
from models import Address, User
from sqlalchemy import select

# conexão com o banco de dados
engine = create_engine("sqlite://")

# criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)

inspetor_engine = inspect(engine)
print(inspetor_engine.get_table_names())
print(inspetor_engine.default_schema_name)

with Session(engine) as session:
    samuel = User(
        name="Samuel",
        fullname="Samuel Oliveir",
        address=[Address(email_address="samuel@gmail.com")]
    )

    test = User(
        name="test",
        fullname="Test Pat",
        address=[Address(email_address="test@gmail.com"), Address(email_address="testc@gmail.com")]
    )

    # enviando para o DB (persistencia de dados)
    session.add_all([samuel, test])
    session.commit()


# (await db_session.execute(select(AtletaModel))).scalars().all()

# stmt = session.execute(select(User)).scalars().all()
# print(stmt)


stmt_join = select(User.fullname, Address.email_address).join_from(Address, User)

print(stmt_join)
for result in session.scalars(stmt_join):
    print(result)

connection = engine.connect()
results = connection.execute(stmt_join).fetchall()
print("Executando statement a partir da connection")
for result in results:
    print(result)
    