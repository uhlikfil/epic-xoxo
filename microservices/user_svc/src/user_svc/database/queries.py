import os

TABLE_NAME = os.getenv("TABLE_NAME")


SELECT_USER = f"SELECT username, origin_ip, last_ip, UNIX_TIMESTAMP(created) FROM {TABLE_NAME} WHERE username = %s"
INSERT_USER = f"INSERT INTO {TABLE_NAME} (username, origin_ip, last_ip) VALUES (%s, %s, %s)"
DELETE_USER = f"DELETE FROM {TABLE_NAME} WHERE username = %s"
UPDATE_USER = f"UPDATE {TABLE_NAME} SET last_ip = %s WHERE username = %s"
