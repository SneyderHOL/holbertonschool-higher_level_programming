#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Class for testing with unit test the function max_integer"""

    def test_max_integer(self):
        """ Test when a integer list is passed to function """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([2]), 2)

    def test_positive_middle(self):
        """Tests for positive max integer in middle"""
        self.assertEqual(max_integer([1, 10, 8, 23, 14, 20]), 23)

    def test_empty_list(self):
        """ Test when an empty list is passed to function """
        self.assertEqual(max_integer([]), None)

    def test_string_value(self):
        """ Test when a string value is passed to function """
        self.assertEqual(max_integer('Hello'), 'o')
        self.assertEqual(max_integer('H'), 'H')

    def test_boolean_list(self):
        """ Test when a boolean list is passed to function """
        self.assertEqual(max_integer([True, False]), True)
        self.assertEqual(max_integer([False, False, False]), False)

    def test_tuple_list(self):
        """ Test when a tuple list is passed to function """
        self.assertEqual(max_integer([(3, 4, 6), (4, 5)]), (4, 5))
        self.assertEqual(max_integer([(2, 1)]), (2, 1))

    def test_tuple_value(self):
        """ Test when a tuple value is passed to function """
        self.assertEqual(max_integer(((3, 4, 6), (4, 5))), (4, 5))
        self.assertEqual(max_integer((3, 6)), 6)

    def test_none_value(self):
        """ Test when a None is passed to function """
        self.assertRaises(TypeError, max_integer, None)

    def test_int_value(self):
        """ Test when an int number is passed to function """
        self.assertRaises(TypeError, max_integer, 2)

    def test_float_value(self):
        """ Test when a float number is passed to function """
        self.assertRaises(TypeError, max_integer, 2.0)
