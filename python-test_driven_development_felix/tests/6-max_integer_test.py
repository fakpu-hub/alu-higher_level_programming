#!/usr/bin/python3
"""Unittests for the max_integer function."""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer."""

    def test_max_at_end(self):
        """Test when the maximum integer is at the end."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Test when the maximum integer is at the beginning."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Test when the maximum integer is in the middle."""
        self.assertEqual(max_integer([1, 5, 3, 2]), 5)

    def test_unsorted_list(self):
        """Test an unsorted list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_single_element(self):
        """Test a list containing one element."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test a list containing negative numbers."""
        self.assertEqual(max_integer([-5, -2, -10]), -2)

    def test_all_negative_numbers(self):
        """Test when every number is negative."""
        self.assertEqual(max_integer([-8, -3, -1, -6]), -1)

    def test_duplicate_maximum(self):
        """Test a list with repeated maximum values."""
        self.assertEqual(max_integer([4, 9, 9, 2]), 9)

    def test_all_equal(self):
        """Test a list where all values are equal."""
        self.assertEqual(max_integer([5, 5, 5]), 5)

    def test_zero(self):
        """Test a list containing zero."""
        self.assertEqual(max_integer([0, -1, -5]), 0)

    def test_float_values(self):
        """Test a list containing floating-point numbers."""
        self.assertEqual(max_integer([1.5, 3.8, 2.4]), 3.8)


if __name__ == "__main__":
    unittest.main()
