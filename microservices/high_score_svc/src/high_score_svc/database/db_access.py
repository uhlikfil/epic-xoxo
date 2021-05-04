import os
from contextlib import contextmanager

import mysql.connector as cn
from high_score_svc.database.queries import (INSERT, SELECT_ONE,
                                             SELECT_ONE_RANKED,
                                             SELECT_TOP_RANKED, UPDATE)
from high_score_svc.models.body import Body

CONNECTION_CONFIG = {
    "host": "high_score_db",
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


def get_top_high_scores() -> list:
    with get_connection() as cnx:
        with cnx.cursor() as cursor:
            cursor.execute(SELECT_TOP_RANKED)
            return cursor.fetchall()


def get_high_score(username: str, ranked: bool) -> tuple:
    with get_connection() as cnx:
        with cnx.cursor() as cursor:
            cursor.execute(SELECT_ONE_RANKED if ranked else SELECT_ONE, (username,))
            return cursor.fetchone()


def create_high_score(username: str, data: Body) -> bool:
    with get_connection() as cnx:
        with cnx.cursor() as cursor:
            cursor.execute(INSERT[data.game_result], (username,))
            return cursor.rowcount == 1


def update_high_score(username: str, data: Body) -> bool:
    with get_connection() as cnx:
        with cnx.cursor() as cursor:
            cursor.execute(UPDATE[data.game_result], (username,))
            return cursor.rowcount == 1
