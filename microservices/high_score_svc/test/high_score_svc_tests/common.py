import os

HOST = "app"
PORT = os.getenv("APP_PORT")
BASE_PATH = "/api/v1"

TESTED_URL = f"http://{HOST}:{PORT}{BASE_PATH}"
