import os

TABLE_NAME = os.getenv("TABLE_NAME")


SELECT_USER = f"SELECT username, email, password_hash, UNIX_TIMESTAMP(created), UNIX_TIMESTAMP(last_updated) FROM {TABLE_NAME} WHERE username = %s"
