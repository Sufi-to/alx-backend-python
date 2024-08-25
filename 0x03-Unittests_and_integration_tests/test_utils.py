#!/usr/bin/env python3
"""Module that contains test cases for the utils.py"""

import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """This is class tests the functions in the utils file"""

    @parameterized.expand([
        {"a": 1}, ("a",),
        {"a": {"b": 2}}, ("a",),
        {"a": {"b": 2}}, ("a", "b")
        ])
    def test_access_nested_map(self, nested_map, path):
        """Tests the access_nested_map function"""
        self.assertEqual(nested_map, path, 1)