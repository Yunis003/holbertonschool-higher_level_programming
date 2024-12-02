#!/usr/bin/python3
""" Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_ordered_list(self):
        """Test with an ordered list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list of integers"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        """Test with a list of one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_all_negative_numbers(self):
        """Test with all negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_list_with_repeated_elements(self):
        """Test with repeated elements"""
        self.assertEqual(max_integer([1, 3, 3, 3, 2]), 3)

if __name__ == '__main__':
    unittest.main()
