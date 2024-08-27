#!/usr/bin/env python3
""" Module for testing the methods in the client file """

from client import GithubOrgClient
from parameterized import parameterized
from unittest import TestCase
from unittest.mock import patch


class TestGithubOrgClient(TestCase):
    """Test class for the GithubOrgClient class"""

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, data, mock):
        """method that tests GithubOrgClient.org returns the correct value"""
        test_class = GithubOrgClient(data)
        test_class.org()
        mock.assert_called_once_with(f'https://api.github.com/orgs/{data}')
