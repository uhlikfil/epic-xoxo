from user_svc.models.user import User
from user_svc.validators.ip import is_valid_ip_address


def is_valid_username(username: str):
    return username is not None and len(username) <= 64


def check_user(user: User) -> bool:
    if not is_valid_username(user.username):
        return False
    if not is_valid_ip_address(user.origin_ip):
        return False
    if not is_valid_ip_address(user.last_ip):
        return False
    return True
