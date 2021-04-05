import connexion
from user_svc.database.db_access import get_user
from user_svc.models.user import User  # noqa: E501
from user_svc.models.user_detail import UserDetail  # noqa: E501


def create_user(body):  # noqa: E501
    """Create a new user

     # noqa: E501

    :param body: Created user object
    :type body: dict | bytes

    :rtype: User
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return "do some magic!"


def delete_user(username):  # noqa: E501
    """Delete user

     # noqa: E501

    :param username: The user that needs to be deleted
    :type username: str

    :rtype: None
    """
    return "do some magic!"


def get_user_by_username(username):  # noqa: E501
    """Get user by username

     # noqa: E501

    :param username: The username that needs to be fetched
    :type username: str

    :rtype: User
    """
    return "do some magic!"


def get_userdetail(username):  # noqa: E501
    """User with other aggregated data

     # noqa: E501

    :param username: The username that needs to be fetched
    :type username: str

    :rtype: UserDetail
    """
    return "do some magic!"


def update_user(body, username):  # noqa: E501
    """Update user

     # noqa: E501

    :param body: Updated user object
    :type body: dict | bytes
    :param username: user that needs to be updated
    :type username: str

    :rtype: User
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return "do some magic!"
