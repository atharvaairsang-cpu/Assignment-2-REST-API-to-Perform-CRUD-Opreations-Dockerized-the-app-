from sqlalchemy import text
from database import engine


def delete_user(id):
    with engine.begin() as connection:
        connection.execute(text("DELETE FROM users WHERE id = :id"), {"id": id})
