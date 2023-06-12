#!/usr/bin/python3
"""This module contains unittest cases for the function 'max_integer'"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class for conducting unittests"""
    def test_max_integer(self):
        """Test cases function"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([7, 1, 2, 3, 4, 5]), 7)
        self.assertEqual(max_integer([1, 2, 9, 4, 5]), 9)
        self.assertEqual(max_integer([1, 2, -3, 4, 8]), 8)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([]), None)
