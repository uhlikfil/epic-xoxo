# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from high_score_svc.models.base_model_ import Model
from high_score_svc import util


class HighScore(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(
        self,
        username: str = None,
        wins: int = None,
        loses: int = None,
        ragequits: int = None,
        winrate: float = None,
        rank: int = None,
    ):  # noqa: E501
        """HighScore - a model defined in Swagger

        :param username: The username of this HighScore.  # noqa: E501
        :type username: str
        :param wins: The wins of this HighScore.  # noqa: E501
        :type wins: int
        :param loses: The loses of this HighScore.  # noqa: E501
        :type loses: int
        :param ragequits: The ragequits of this HighScore.  # noqa: E501
        :type ragequits: int
        :param winrate: The winrate of this HighScore.  # noqa: E501
        :type winrate: float
        :param rank: The rank of this HighScore.  # noqa: E501
        :type rank: int
        """
        self.swagger_types = {
            "username": str,
            "wins": int,
            "loses": int,
            "ragequits": int,
            "winrate": float,
            "rank": int,
        }

        self.attribute_map = {
            "username": "username",
            "wins": "wins",
            "loses": "loses",
            "ragequits": "ragequits",
            "winrate": "winrate",
            "rank": "rank",
        }
        self._username = username
        self._wins = wins
        self._loses = loses
        self._ragequits = ragequits
        self._winrate = winrate
        self._rank = rank

    @classmethod
    def from_dict(cls, dikt) -> "HighScore":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The HighScore of this HighScore.  # noqa: E501
        :rtype: HighScore
        """
        return util.deserialize_model(dikt, cls)

    @property
    def username(self) -> str:
        """Gets the username of this HighScore.


        :return: The username of this HighScore.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this HighScore.


        :param username: The username of this HighScore.
        :type username: str
        """

        self._username = username

    @property
    def wins(self) -> int:
        """Gets the wins of this HighScore.


        :return: The wins of this HighScore.
        :rtype: int
        """
        return self._wins

    @wins.setter
    def wins(self, wins: int):
        """Sets the wins of this HighScore.


        :param wins: The wins of this HighScore.
        :type wins: int
        """

        self._wins = wins

    @property
    def loses(self) -> int:
        """Gets the loses of this HighScore.


        :return: The loses of this HighScore.
        :rtype: int
        """
        return self._loses

    @loses.setter
    def loses(self, loses: int):
        """Sets the loses of this HighScore.


        :param loses: The loses of this HighScore.
        :type loses: int
        """

        self._loses = loses

    @property
    def ragequits(self) -> int:
        """Gets the ragequits of this HighScore.


        :return: The ragequits of this HighScore.
        :rtype: int
        """
        return self._ragequits

    @ragequits.setter
    def ragequits(self, ragequits: int):
        """Sets the ragequits of this HighScore.


        :param ragequits: The ragequits of this HighScore.
        :type ragequits: int
        """

        self._ragequits = ragequits

    @property
    def winrate(self) -> float:
        """Gets the winrate of this HighScore.


        :return: The winrate of this HighScore.
        :rtype: float
        """
        return self._winrate

    @winrate.setter
    def winrate(self, winrate: float):
        """Sets the winrate of this HighScore.


        :param winrate: The winrate of this HighScore.
        :type winrate: float
        """

        self._winrate = winrate

    @property
    def rank(self) -> int:
        """Gets the rank of this HighScore.


        :return: The rank of this HighScore.
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank: int):
        """Sets the rank of this HighScore.


        :param rank: The rank of this HighScore.
        :type rank: int
        """

        self._rank = rank
