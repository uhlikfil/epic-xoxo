import os
from contextlib import contextmanager

import mysql.connector as cn
from high_score_svc.database.queries import DELETE, INSERT, SELECT, UPDATE

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
