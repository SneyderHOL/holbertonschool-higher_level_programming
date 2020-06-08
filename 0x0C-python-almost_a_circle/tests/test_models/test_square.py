#!/usr/bin/python3
"""Unittest for Rectangle"""
import unittest
from models import square
from models.square import Square
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """ Class for testing with unit test the Square class"""

    def test_docstrings(self):
        """Tests for dosctrings"""
        self.assertGreater(len(square.__doc__), 1)
        self.assertGreater(len(Square.__doc__), 1)
        self.assertGreater(len(Square.__init__.__doc__), 1)
        self.assertGreater(len(Square.__str__.__doc__), 1)

    def test_new_object(self):
        """ Test when an instance is created"""
        square_obj = Square(10, 2, 1, 5)
        self.assertTrue(issubclass(type(square_obj), Rectangle))
        self.assertIsInstance(square_obj, Square)
        self.assertEqual(square_obj.id, 5)
        self.assertEqual(square_obj.width, 10)
        self.assertEqual(square_obj.height, 10)
        self.assertEqual(square_obj.x, 2)
        self.assertEqual(square_obj.y, 1)
        square_obj2 = Square(2, 10, 0, 1)
        self.assertEqual(square_obj2.id, 1)
        self.assertEqual(square_obj2.width, 2)
        self.assertEqual(square_obj2.height, 2)
        self.assertEqual(square_obj2.x, 10)
        self.assertEqual(square_obj2.y, 0)
        with self.assertRaises(TypeError):
            square_obj1 = Square()


    def test_area_validations(self):
        """Tests for area method"""
        square_obj2 = Square(2, 10, 0, 3)
        self.assertEqual(square_obj2.area(), 4)
        with self.assertRaises(TypeError):
            square_obj2.area(45)

    def test__str__validations(self):
        """Tests for __str__ method"""
        square_obj3 = Square(10, 2, 1, 1)
        self.assertEqual(square_obj3.__str__(), '[Square] (1) 2/1 - 10')
        with self.assertRaises(TypeError):
            square_obj3.__str__([2, 4])

    def test_size__setter_validation(self):
        """Tests for size setter method"""
        square_obj4 = Square(5, 3, 1, 12)
        square_obj4.size = 3
        self.assertEqual(square_obj4.size, 3)

    def test_size__getter_validation(self):
        """Tests for size getter method"""
        square_obj5 = Square(7, 3, 1, 12)
        self.assertEqual(square_obj5.size, 7)
        with self.assertRaises(TypeError):
            square_obj5.size = [2, 4]
        with self.assertRaises(ValueError):
            square_obj5.size = -5

    def test_update_validations(self):
        """Tests for update method"""
        square_obj6 = Square(1, 1, 1, 1)
        square_obj6.update(89)
        self.assertEqual(square_obj6.id, 89)
        square_obj6.update(89, 2)
        self.assertEqual(square_obj6.size, 2)
        square_obj6.update(89, 2, 3)
        self.assertEqual(square_obj6.x, 3)
        square_obj6.update(89, 2, 3, 4)
        self.assertEqual(square_obj6.y, 4)
#
        with self.assertRaises(TypeError):
            square_obj6.update(1, True)
        with self.assertRaises(TypeError):
            square_obj6.update(89, [1])
        with self.assertRaises(ValueError):
            square_obj6.update(89, 2, -3)
        with self.assertRaises(TypeError):
            square_obj6.update(89, 2, 3, 5.5)
        square_obj6.update(23, 2, 3, id=9, size=8)
        self.assertEqual(square_obj6.id, 23)
        self.assertEqual(square_obj6.size, 2)
        with self.assertRaises(TypeError):
            square_obj6.update(size=True)
        square_obj6.update(size=9, y=8)
        self.assertEqual(square_obj6.size, 9)
        self.assertEqual(square_obj6.y, 8)

    def test_to_dictionary_validations(self):
        """Tests for to_dictionary method"""
        square_obj7 = Square(4, 2, 1, 6)
        aux = {'id': 6, 'size': 4, 'x': 2, 'y': 1}
        self.assertEqual(sorted(square_obj7.to_dictionary()), sorted(aux))
        self.assertEqual(type(square_obj7.to_dictionary()), dict)
        with self.assertRaises(TypeError):
            square_obj7.to_dictionary(89, True, 3, 5.5)

if __name__ == '__main__':
    unittest.main()
