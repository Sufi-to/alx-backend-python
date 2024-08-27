#!/usr/bin/env python3
"""Module that contains test cases for the utils.py"""

import requests
from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(TestCase):
    """This is class tests the functions in the utils file"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Tests the access_nested_map function"""
        res = access_nested_map(nested_map, path)
        self.assertEqual(res, expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
        ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Context manager to test that a KeyError is raised"""
        with self.assertRaises(KeyError) as E:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(E.exception))


class TestGetJson(TestCase):
    """Test class for get_json method"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, url, expected_result, mock_get):
        """Method to test that utils.get_json returns the expected result."""
        mock_get.return_value.json.return_value = expected_result
        result = get_json(url)
        self.assertEqual(result, expected_result)
        mock_get.assert_called_once_with(url)


class TestMemoize(TestCase):
    """Test class the memoize method"""

    def test_memoize(self):
        """Method to test"""

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        res = TestClass()

        result1 = res.a_property
        result2 = res.a_property

        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)
