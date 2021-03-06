# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from high_score_svc.models.base_model_ import Model
from high_score_svc.models.high_score import HighScore  # noqa: F401,E501
from high_score_svc import util


class HighScoreArray(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, high_scores: List[HighScore] = None):  # noqa: E501
        """HighScoreArray - a model defined in Swagger

        :param high_scores: The high_scores of this HighScoreArray.  # noqa: E501
        :type high_scores: List[HighScore]
        """
        self.swagger_types = {"high_scores": List[HighScore]}

        self.attribute_map = {"high_scores": "high_scores"}
        self._high_scores = high_scores

    @classmethod
    def from_dict(cls, dikt) -> "HighScoreArray":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The HighScoreArray of this HighScoreArray.  # noqa: E501
        :rtype: HighScoreArray
        """
        return util.deserialize_model(dikt, cls)

    @property
    def high_scores(self) -> List[HighScore]:
        """Gets the high_scores of this HighScoreArray.


        :return: The high_scores of this HighScoreArray.
        :rtype: List[HighScore]
        """
        return self._high_scores

    @high_scores.setter
    def high_scores(self, high_scores: List[HighScore]):
        """Sets the high_scores of this HighScoreArray.


        :param high_scores: The high_scores of this HighScoreArray.
        :type high_scores: List[HighScore]
        """

        self._high_scores = high_scores
