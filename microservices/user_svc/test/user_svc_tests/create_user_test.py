import requests

from common import TESTED_URL

URL = f"{TESTED_URL}/user"


def create_user(name: str = "test", ip: str = "192.168.1.1"):
    user = {"username": name, "origin_ip": ip, "last_ip": ip}
    return requests.post(URL, json=user)


def test_valid_new_user():
    new_username = "newboy"
    resp = create_user(new_username)
    assert resp.status_code == 200
    assert resp.json()["username"] == new_username


def test_invalid_username():
    username = "verylongname" * 10
    resp = create_user(username)
    assert resp.status_code == 422


def test_invalid_ip():
    ip = "totally ip address"
    resp = create_user(ip=ip)
    assert resp.status_code == 422


def test_invalid_json():
    bad_json = {
        "usernamee": "test",
        "hehe": 12,
    }
    resp = requests.post(URL, json=bad_json)
    assert resp.status_code == 422


def test_existing_user():
    create_user()
    resp = create_user()
    assert resp.status_code == 409


def test_read_only_attributes():
    user = {
        "username": "badboy",
        "origin_ip": "192.168.1.1",
        "last_ip": "192.168.1.1",
        "created": 1,
    }
    resp = requests.post(URL, json=user)
    assert resp.status_code == 400
