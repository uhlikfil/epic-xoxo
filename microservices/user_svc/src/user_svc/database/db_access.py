import os
from contextlib import contextmanager

import mysql.connector as cn
from user_svc.database.queries import SELECT_USER
from user_svc.models import User

CONNECTION_CONFIG = {
    "host": "user_db",
    "port": os.getenv("MYSQL_TCP_PORT"),
    "user": os.getenv("MYSQL_USER"),
    "password": os.getenv("MYSQL_PASSWORD"),
    "database": os.getenv("MYSQL_DATABASE"),
}

@contextmanager
def get_connection():
    cnx = cn.connect(**CONNECTION_CONFIG)
    try:
        yield cnx
    finally:
        cnx.close()


def get_user(username: str) -> tuple:
    with get_connection() as cnx:
        with cnx.cursor() as cursor:
            cursor.execute(SELECT_USER, (username, ))
            return cursor.fetchone()
