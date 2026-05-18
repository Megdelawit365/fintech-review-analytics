from sqlalchemy import text
from db_connection import engine

with open("sql/schema.sql", "r") as file:
    schema = file.read()

with engine.connect() as connection:
    connection.execute(text(schema))
    connection.commit()

print("Tables created")
