import high_score_svc.database.db_access as db
import high_score_svc.validators as valid
from high_score_svc.models.body import Body  # noqa: E501
from high_score_svc.models.high_score import HighScore  # noqa: E501
from high_score_svc.models.high_score_array import HighScoreArray  # noqa: E501
from werkzeug.exceptions import NotFound, UnprocessableEntity


def __err_invalid_data():
    raise UnprocessableEntity("Invalid data supplied")


def __err_not_found():
    raise NotFound("The user doesn't exist or hasn't played 10 games yet")


def get_high_score_top():  # noqa: E501
    """Get the top 10 users

     # noqa: E501


    :rtype: HighScoreArray
    """
    return HighScoreArray([HighScore(*score) for score in db.get_top_high_scores()])


def get_user_high_score(username):  # noqa: E501
    """Get the ranking of the desired user

     # noqa: E501

    :param username: The username that needs to be fetched
    :type username: str

    :rtype: HighScore
    """
    if not valid.is_valid_username(username):
        __err_invalid_data()
    high_score_data = db.get_high_score(username, True)
    if not high_score_data:
        __err_not_found()
    return HighScore(*high_score_data)
