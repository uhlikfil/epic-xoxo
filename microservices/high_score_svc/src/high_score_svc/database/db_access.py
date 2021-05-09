import enum
import os
from contextlib import contextmanager

import mysql.connector as cn
from high_score_svc.database.queries import (
    DELETE,
    INSERT,
    SELECT_ONE,
    SELECT_ONE_RANKED,
    SELECT_TOP_RANKED,
    UPDATE,
)
from high_score_svc.logger import PrintLogger

LOGGER = PrintLogger("DB_ACCESS")


class GameResult(enum.Enum):
    WIN = "win"
    LOSE = "lose"
    RAGEQUIT = "ragequit"


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
    LOGGER.log("Getting top high scores")
    with get_connection() as cnx:
        with cnx.cursor() as cursor:
            cursor.execute(SELECT_TOP_RANKED)
            return cursor.fetchall()


def get_high_score(username: str, ranked: bool) -> tuple:
    LOGGER.log(f"Getting high score of {username} (ranked only: {ranked})")
    with get_connection() as cnx:
        with cnx.cursor() as cursor:
            cursor.execute(SELECT_ONE_RANKED if ranked else SELECT_ONE, (username,))
            return cursor.fetchone()


def create_high_score(username: str, game_result: GameResult) -> bool:
    LOGGER.log(f"Creating new high score for {username} - {game_result.value}")
    with get_connection() as cnx:
        with cnx.cursor() as cursor:
            cursor.execute(INSERT[game_result.value], (username,))
            return cursor.rowcount == 1


def update_high_score(username: str, game_result: GameResult) -> bool:
    LOGGER.log(f"Updating high score of {username} - {game_result.value}")
    with get_connection() as cnx:
        with cnx.cursor() as cursor:
            cursor.execute(UPDATE[game_result.value], (username,))
            return cursor.rowcount == 1


def delete_high_score(username: str) -> bool:
    LOGGER.log(f"Deleting high score of {username}")
    with get_connection() as cnx:
        with cnx.cursor() as cursor:
            cursor.execute(DELETE, (username,))
            return cursor.rowcount == 1
