# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from high_score_svc.models.body import Body  # noqa: E501
from high_score_svc.models.error import Error  # noqa: E501
from high_score_svc.models.high_score import HighScore  # noqa: E501
from high_score_svc.models.inline_response200 import InlineResponse200  # noqa: E501
from high_score_svc.test import BaseTestCase


class TestHighScoreController(BaseTestCase):
    """HighScoreController integration test stubs"""

    def test_get_high_score_top(self):
        """Test case for get_high_score_top

        Get the top 10 users
        """
        response = self.client.open(
            '/api/v1/high_score',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user_high_score(self):
        """Test case for get_user_high_score

        Get the ranking of the desired user
        """
        response = self.client.open(
            '/api/v1/high_score/{username}'.format(username='username_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_high_score_update(self):
        """Test case for post_high_score_update

        Increment the win/loss/ragequit count for the desired user
        """
        body = Body()
        response = self.client.open(
            '/api/v1/high_score/{username}'.format(username='username_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
