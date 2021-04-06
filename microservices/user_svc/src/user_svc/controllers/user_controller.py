import re

import connexion
import user_svc.database.db_access as db
import user_svc.validators as valid
from user_svc.models.body import Body  # noqa: E501
from user_svc.models.error import Error
from user_svc.models.user import User  # noqa: E501
from user_svc.models.user_detail import UserDetail  # noqa: E501


def __err(msg: str, status: int):
    return Error(msg), status


def __err_invalid_data():
    return __err("Invalid data supplied", 400)


def __err_already_exists():
    return __err("User already exists", 409)


def __err_not_found():
    return __err("User not found", 404)


def create_user(body):  # noqa: E501
    """Create a new user

     # noqa: E501

    :param body: User to create
    :type body: dict | bytes

    :rtype: User
    """
    user = User.from_dict(body)  # noqa: E501
    if not valid.check_user(user):
        return __err_invalid_data()
    if not db.insert_user(user):
        return __err_already_exists()
    return get_user_by_username(user.username)


def delete_user(username):  # noqa: E501
    """Delete user

     # noqa: E501

    :param username: The user that needs to be deleted
    :type username: str

    :rtype: None
    """
    if not valid.is_valid_username(username):
        return __err_invalid_data()
    if not db.delete_user(username):
        return __err_not_found()
    return "", 204


def get_user_by_username(username):  # noqa: E501
    """Get user by username

     # noqa: E501

    :param username: The username that needs to be fetched
    :type username: str

    :rtype: User
    """
    if not valid.is_valid_username(username):
        return __err_invalid_data()
    user_data = db.get_user(username)
    if not user_data:
        return __err_not_found()
    return User(*user_data)


def get_userdetail(username):  # noqa: E501
    """User with other aggregated data

     # noqa: E501

    :param username: The username that needs to be fetched
    :type username: str

    :rtype: UserDetail
    """
    return 'not yet implemented'


def update_user(body, username):  # noqa: E501
    """Update user

     # noqa: E501

    :param body: The last IP to update
    :type body: dict | bytes
    :param username: user that needs to be updated
    :type username: str

    :rtype: User
    """
    if not valid.is_valid_username(username):
        return __err_invalid_data()
    body = Body.from_dict(connexion.request.get_json())  # noqa: E501
    if not valid.is_valid_ip_address(body.ip):
        return __err_invalid_data()
    if not db.update_user(username, body.ip):
        return __err_not_found()
    return get_user_by_username(username)