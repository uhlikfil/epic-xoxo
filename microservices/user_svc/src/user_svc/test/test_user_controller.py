# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from user_svc.models.user import User  # noqa: E501
from user_svc.models.user_detail import UserDetail  # noqa: E501
from user_svc.test import BaseTestCase


class TestUserController(BaseTestCase):
    """UserController integration test stubs"""

    def test_create_user(self):
        """Test case for create_user

        Create a new user
        """
        body = User()
        response = self.client.open(
            "/api/v1/user",
            method="POST",
            data=json.dumps(body),
            content_type="application/json",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_delete_user(self):
        """Test case for delete_user

        Delete user
        """
        response = self.client.open(
            "/api/v1/user/{username}".format(username="username_example"),
            method="DELETE",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_get_user_by_username(self):
        """Test case for get_user_by_username

        Get user by username
        """
        response = self.client.open(
            "/api/v1/user/{username}".format(username="username_example"), method="GET"
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_get_userdetail(self):
        """Test case for get_userdetail

        User with other aggregated data
        """
        response = self.client.open(
            "/api/v1/userdetail/{username}".format(username="username_example"),
            method="GET",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_update_user(self):
        """Test case for update_user

        Update user
        """
        body = User()
        response = self.client.open(
            "/api/v1/user/{username}".format(username="username_example"),
            method="PUT",
            data=json.dumps(body),
            content_type="application/json",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))


if __name__ == "__main__":
    import unittest

    unittest.main()
