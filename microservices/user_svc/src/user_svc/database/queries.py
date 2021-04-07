import os

TABLE_NAME = os.getenv("TABLE_NAME")

# fmt: off
SELECT = f"SELECT username, origin_ip, last_ip, UNIX_TIMESTAMP(created) FROM {TABLE_NAME} WHERE username = %s"
INSERT = f"INSERT INTO {TABLE_NAME} (username, origin_ip, last_ip) VALUES (%s, %s, %s)"
DELETE = f"DELETE FROM {TABLE_NAME} WHERE username = %s"
UPDATE = f"UPDATE {TABLE_NAME} SET last_ip = %s WHERE username = %s"
