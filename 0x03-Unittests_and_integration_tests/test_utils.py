#!/usr/bin/env python3
"""Module that contains test cases for the utils.py"""

import unittest
from parameterized import parameterized
access_map = __import__('utils').access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """This is class tests the functions in the utils file"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Tests the access_nested_map function"""
        res = access_map(nested_map, path)
        self.assertEqual(res, expected)
