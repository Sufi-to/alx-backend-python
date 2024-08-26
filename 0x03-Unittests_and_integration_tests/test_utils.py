#!/usr/bin/env python3
"""Module that contains test cases for the utils.py"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
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
