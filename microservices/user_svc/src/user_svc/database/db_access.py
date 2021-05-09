import os
from contextlib import contextmanager

import mysql.connector as cn
from user_svc.database.queries import DELETE, INSERT, SELECT, UPDATE
from user_svc.logger import PrintLogger
from user_svc.models import User

LOGGER = PrintLogger("DB_ACCESS")

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
        cnx.commit()
        cnx.close()


def get_user(username: str) -> tuple:
    LOGGER.log(f"Getting user {username}")
    with get_connection() as cnx:
        with cnx.cursor() as cursor:
            cursor.execute(SELECT, (username,))
            return cursor.fetchone()


def insert_user(user: User) -> bool:
    LOGGER.log(f"Creating a new user {user}")
    with get_connection() as cnx:
        with cnx.cursor() as cursor:
            try:
                cursor.execute(INSERT, (user.username, user.origin_ip, user.last_ip))
                return cursor.rowcount == 1
            except cn.errors.IntegrityError:
                return False


def delete_user(username: str) -> bool:
    LOGGER.log(f"Deleting user {username}")
    with get_connection() as cnx:
        with cnx.cursor() as cursor:
            cursor.execute(DELETE, (username,))
            return cursor.rowcount == 1


def update_user(username: str, new_ip: str) -> bool:
    LOGGER.log(f"Updating user {username} with IP {new_ip}")
    with get_connection() as cnx:
        with cnx.cursor() as cursor:
            cursor.execute(UPDATE, (new_ip, username))
            return cursor.rowcount == 1
