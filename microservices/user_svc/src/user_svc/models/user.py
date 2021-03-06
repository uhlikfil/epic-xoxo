# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from user_svc.models.base_model_ import Model
from user_svc import util


class User(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(
        self,
        username: str = None,
        origin_ip: str = None,
        last_ip: str = None,
        created: int = None,
        updated: int = None,
    ):  # noqa: E501
        """User - a model defined in Swagger

        :param username: The username of this User.  # noqa: E501
        :type username: str
        :param origin_ip: The origin_ip of this User.  # noqa: E501
        :type origin_ip: str
        :param last_ip: The last_ip of this User.  # noqa: E501
        :type last_ip: str
        :param created: The created of this User.  # noqa: E501
        :type created: int
        :param updated: The updated of this User.  # noqa: E501
        :type updated: int
        """
        self.swagger_types = {
            "username": str,
            "origin_ip": str,
            "last_ip": str,
            "created": int,
            "updated": int,
        }

        self.attribute_map = {
            "username": "username",
            "origin_ip": "origin_ip",
            "last_ip": "last_ip",
            "created": "created",
            "updated": "updated",
        }
        self._username = username
        self._origin_ip = origin_ip
        self._last_ip = last_ip
        self._created = created
        self._updated = updated

    @classmethod
    def from_dict(cls, dikt) -> "User":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The User of this User.  # noqa: E501
        :rtype: User
        """
        return util.deserialize_model(dikt, cls)

    @property
    def username(self) -> str:
        """Gets the username of this User.


        :return: The username of this User.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this User.


        :param username: The username of this User.
        :type username: str
        """

        self._username = username

    @property
    def origin_ip(self) -> str:
        """Gets the origin_ip of this User.


        :return: The origin_ip of this User.
        :rtype: str
        """
        return self._origin_ip

    @origin_ip.setter
    def origin_ip(self, origin_ip: str):
        """Sets the origin_ip of this User.


        :param origin_ip: The origin_ip of this User.
        :type origin_ip: str
        """

        self._origin_ip = origin_ip

    @property
    def last_ip(self) -> str:
        """Gets the last_ip of this User.


        :return: The last_ip of this User.
        :rtype: str
        """
        return self._last_ip

    @last_ip.setter
    def last_ip(self, last_ip: str):
        """Sets the last_ip of this User.


        :param last_ip: The last_ip of this User.
        :type last_ip: str
        """

        self._last_ip = last_ip

    @property
    def created(self) -> int:
        """Gets the created of this User.


        :return: The created of this User.
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created: int):
        """Sets the created of this User.


        :param created: The created of this User.
        :type created: int
        """

        self._created = created

    @property
    def updated(self) -> int:
        """Gets the updated of this User.


        :return: The updated of this User.
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated: int):
        """Sets the updated of this User.


        :param updated: The updated of this User.
        :type updated: int
        """

        self._updated = updated
