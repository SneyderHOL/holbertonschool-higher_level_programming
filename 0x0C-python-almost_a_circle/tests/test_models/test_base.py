#!/usr/bin/python3
"""Unittest for Base"""
import unittest
Base = __import__('models.base').Base
#import models
#Base = models.base.Base

class TestBase(unittest.TestCase):
    """ Class for testing with unit test the Base class"""

    def test_instance(self):
        """ Test when an instance is created"""
        obj = Base()
        self.assertisInstance(obj, Base)
        self.assertEqual(obj.id, 1)

if __name__ == '__main__':
    unittest.main()
