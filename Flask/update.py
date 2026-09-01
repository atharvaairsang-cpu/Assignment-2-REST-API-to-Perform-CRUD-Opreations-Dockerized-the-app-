from sqlalchemy import text
from database import engine


def update_user(id, data):
    data["id"] = id
    with engine.begin() as connection:
        connection.execute(
            text("UPDATE users SET city=:city, country=:country, temperature=:temperature, "
                 "humidity=:humidity, wind_speed=:wind_speed WHERE id=:id"),
            data
        )
