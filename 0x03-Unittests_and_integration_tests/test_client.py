#!/usr/bin/env python3
""" Module for testing the methods in the client file """

from client import GithubOrgClient
from parameterized import parameterized
from unittest import TestCase
from unittest.mock import patch, PropertyMock
from typing import Dict


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

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """Tests the repo"""
        payload = [{"name": "Google"}, {"name": "Twitter"}]
        mock_json.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public:

            mock_public.return_value = "hello/world"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()

            check = [i["name"] for i in payload]
            self.assertEqual(result, check)

            mock_public.assert_called_once()
            mock_json.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': "bsd-3-clause"}}, "bsd-3-clause", True),
        ({'license': {'key': "bsl-1.0"}}, "bsd-3-clause", False),
    ])
    def test_has_license(self, repo: Dict, key: str, expected: bool) -> None:
        """Test if the has_licence works fine"""
        client_org = GithubOrgClient("google")
        has_licence = client_org.has_license(repo, key)
        self.assertEqual(has_licence, expected)
