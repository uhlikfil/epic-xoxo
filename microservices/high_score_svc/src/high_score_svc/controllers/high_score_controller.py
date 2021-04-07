import connexion
import six

from high_score_svc.models.body import Body  # noqa: E501
from high_score_svc.models.error import Error  # noqa: E501
from high_score_svc.models.high_score import HighScore  # noqa: E501
from high_score_svc.models.high_score_array import HighScoreArray  # noqa: E501
from high_score_svc import util


def get_high_score_top():  # noqa: E501
    """Get the top 10 users

     # noqa: E501


    :rtype: HighScoreArray
    """
    return "do some magic!"


def get_user_high_score(username):  # noqa: E501
    """Get the ranking of the desired user

     # noqa: E501

    :param username: The username that needs to be fetched
    :type username: str

    :rtype: HighScore
    """
    return "do some magic!"


def post_high_score_update(body, username):  # noqa: E501
    """Increment the win/loss/ragequit count for the desired user

     # noqa: E501

    :param body: Whether the user has won, lost or ragequit
    :type body: dict | bytes
    :param username: The username that needs to be updated
    :type username: str

    :rtype: HighScore
    """
    if connexion.request.is_json:
        body = Body.from_dict(connexion.request.get_json())  # noqa: E501
    return "do some magic!"
