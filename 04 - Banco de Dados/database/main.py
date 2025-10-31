import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conn = sqlite3.connect(ROOT_PATH / "clientes.db")
cursor = conn.cursor()


def create_table(conn, cursor, table_name):
    cursor.execute(
        f"CREATE TABLE {table_name}"
        "(id INTEGER PRIMARY KEY AUTOINCREMENT," \
        "nome VARCHAR(100), " \
        "email VARCHAR(150))"
    )

def atualizar_registro(conn, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
    conn.commit()

def deletar_registro(conn, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?;", data)
    conn.commit()
    

# atualizar_registro(conn, cursor, "Ninja", "email", id)