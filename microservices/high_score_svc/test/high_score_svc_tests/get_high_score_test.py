import requests

from common import TESTED_URL

URL = f"{TESTED_URL}/high_score"


def test_top_high_scores():
    resp = requests.get(URL)
    assert resp.status_code == 200
    assert isinstance(resp.json()["high_scores"], list)


def test_non_existing_user():
    resp = requests.get(f"{URL}/nobody")
    assert resp.status_code == 404


def test_unranked_user():
    existing_user_url = f"{URL}/unranked"
    game_res = {"game_result": "won"}
    requests.post(existing_user_url, json=game_res)
    resp = requests.get(existing_user_url)
    assert resp.status_code == 404


def test_ranked_user():
    existing_user_url = f"{URL}/ranked"
    for _ in range(10):
        game_res = {"game_result": "won"}
        requests.post(existing_user_url, json=game_res)
    resp = requests.get(existing_user_url)
    assert resp.status_code == 200
    assert resp.json()["username"] == "ranked"


def test_invalid_username():
    invalid = "verylongname" * 10
    resp = requests.get(f"{URL}/{invalid}")
    assert resp.status_code == 422
