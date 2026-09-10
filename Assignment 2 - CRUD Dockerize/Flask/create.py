from sqlalchemy import text
from database import engine


def create_user(data):
    with engine.begin() as connection:
        connection.execute(
            text("INSERT INTO users (city, country, temperature, humidity, wind_speed) "
                 "VALUES (:city, :country, :temperature, :humidity, :wind_speed)"),
            data
        )
