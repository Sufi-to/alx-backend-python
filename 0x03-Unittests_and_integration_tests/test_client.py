#!/usr/bin/env python3
""" Module for testing the methods in the client file """

from client import GithubOrgClient
from parameterized import parameterized
from unittest import TestCase
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(TestCase):
    """Test class for the GithubOrgClient class"""

    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @patch('client.get_json')
    def test_org(self, mock, data):
        """method that tests GithubOrgClient.org returns the correct value"""
        test_class = GithubOrgClient(data)
        test_class.org()
        mock.assert_called_once_with(f'https://api.github.com/orgs/{data}')

    def test_public_repos_url(self):
        """ Test that the result of _public_repos_url yields the expected
            result
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_data:
            payload = {"repos_url": "World"}
            mock_data.return_value = payload
            test_class = GithubOrgClient('test')
            res = test_class._public_repos_url
            self.assertEqual(res, payload["repos_url"])
