import os
from contextlib import contextmanager

import mysql.connector as cn
from user_svc.database.queries import DELETE_USER, INSERT_USER, SELECT_USER, UPDATE_USER
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
        cnx.commit()
        cnx.close()


def get_user(username: str) -> tuple:
    with get_connection() as cnx:
        with cnx.cursor() as cursor:
            cursor.execute(SELECT_USER, (username,))
            return cursor.fetchone()


def insert_user(user: User) -> bool:
    with get_connection() as cnx:
        with cnx.cursor() as cursor:
            try:
                cursor.execute(
                    INSERT_USER, (user.username, user.origin_ip, user.last_ip)
                )
                return cursor.rowcount == 1
            except cn.errors.IntegrityError:
                return False


def delete_user(username: str) -> bool:
    with get_connection() as cnx:
        with cnx.cursor() as cursor:
            cursor.execute(DELETE_USER, (username,))
            return cursor.rowcount == 1


def update_user(username: str, new_ip: str) -> bool:
    with get_connection() as cnx:
        with cnx.cursor() as cursor:
            cursor.execute(UPDATE_USER, (new_ip, username))
            return cursor.rowcount == 1
