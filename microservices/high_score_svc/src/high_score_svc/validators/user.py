from high_score_svc.models.high_score import HighScore


def is_valid_username(username: str):
    return len(username) <= 64
