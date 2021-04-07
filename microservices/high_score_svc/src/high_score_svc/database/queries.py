import os

TABLE_NAME = os.getenv("TABLE_NAME")

# fmt: off
SELECT_ONE = f"SELECT * FROM {TABLE_NAME} WHERE username = %s"
SELECT_TOP = f""
INSERT = f"INSERT INTO {TABLE_NAME} (username, %s) VALUES (%s, %s)"
UPDATE = f"UPDATE {TABLE_NAME} SET %s = %s + 1 WHERE username = %s"
