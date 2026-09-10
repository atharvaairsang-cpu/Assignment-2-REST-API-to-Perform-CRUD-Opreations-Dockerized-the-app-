from sqlalchemy import text
from database import engine


def get_users():
    with engine.connect() as connection:
        rows = connection.execute(text("SELECT * FROM users")).fetchall()
    return [dict(row._mapping) for row in rows]


def get_user(id):
    with engine.connect() as connection:
        row = connection.execute(text("SELECT * FROM users WHERE id = :id"), {"id": id}).fetchone()
    return dict(row._mapping) if row else None
