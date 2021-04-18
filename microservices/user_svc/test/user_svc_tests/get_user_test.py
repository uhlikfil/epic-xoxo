import requests

from common import TESTED_URL
from create_user_test import create_user

URL = f"{TESTED_URL}/user"

def test_existing_user():
    username = "hello"
    create_user(username)
    resp = requests.get(f"{URL}/{username}")
    assert resp.status_code == 200
    assert resp.json()["username"] == username    


def test_non_existing_user():
    resp = requests.get(f"{URL}/nobody")
    assert resp.status_code == 404


def test_invalid_url_params():
    resp = requests.get(f"{URL}/test/test")
    assert resp.status_code == 404


def test_invalid_username():
    username = "verylongname" * 10
    resp = requests.get(f"{URL}/{username}")
    assert resp.status_code == 422
