#!/usr/bin/python3
"""Unittest for Rectangle"""
import unittest
import pep8
from models import rectangle
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
from unittest.mock import patch


class TestRectangle(unittest.TestCase):
    """Class for testing with unit test the Rectangle class"""

    def test_docstrings(self):
        """Tests for dosctrings"""
        self.assertGreater(len(rectangle.__doc__), 1)
        self.assertGreater(len(Rectangle.__doc__), 1)
        self.assertGreater(len(Rectangle.__init__.__doc__), 1)
        self.assertGreater(len(Rectangle.__str__.__doc__), 1)
        self.assertGreater(len(Rectangle.to_dictionary.__doc__), 1)
        self.assertGreater(len(Rectangle.area.__doc__), 1)
        self.assertGreater(len(Rectangle.update.__doc__), 1)
        self.assertGreater(len(Rectangle.display.__doc__), 1)

    def test_pep8(self):
        """ Test for PEP8 """
        pep8_val = pep8.StyleGuide(quiet=True)
        res_rectangle = pep8_val.check_files(['models/rectangle.py'])
        self.assertEqual(res_rectangle.total_errors, 0)
        res_t_r = pep8_val.check_files(['tests/test_models/test_rectangle.py'])
        self.assertEqual(res_t_r.total_errors, 0)

    def test_new_object(self):
        """Tests for an new object"""
        rectangle_obj = Rectangle(10, 2, 1, 1, 12)
        self.assertTrue(issubclass(type(rectangle_obj), Base))
        self.assertIsInstance(rectangle_obj, Rectangle)
        self.assertEqual(rectangle_obj.id, 12)
        self.assertEqual(rectangle_obj.width, 10)
        self.assertEqual(rectangle_obj.height, 2)
        self.assertEqual(rectangle_obj.x, 1)
        self.assertEqual(rectangle_obj.y, 1)
        with self.assertRaises(TypeError):
            rectangle_obj1 = Rectangle()
        with self.assertRaises(TypeError):
            rectangle_obj1 = Rectangle(2, 3, 5, 5, 9, 0, 1)
        with self.assertRaises(TypeError):
            rectangle_obj1 = Rectangle((1, 2, 3, 4, 5))
        with self.assertRaises(ValueError):
            rectangle_obj1 = Rectangle(0, 2, 1, 1, 23)
        with self.assertRaises(TypeError):
            rectangle_obj1 = Rectangle(1, 2.3, 1, 1, 23)

    def test_width_setter_validations(self):
        """Tests for width setter methods"""
        rectangle_obj1 = Rectangle(3, 4, 0, 0, 10)
        with self.assertRaises(ValueError):
            rectangle_obj1.width = 0
        with self.assertRaises(ValueError):
            rectangle_obj1.width = -1
        with self.assertRaises(TypeError):
            rectangle_obj1.width = 'Ho'
        rectangle_obj1.width = 5
        self.assertEqual(rectangle_obj1.width, 5)

    def test_width_getter_validations(self):
        """Tests for width getter methods"""
        rectangle_obj1 = Rectangle(3, 4, 0, 0, 10)
        self.assertEqual(rectangle_obj1.width, 3)

    def test_height_setter_validations(self):
        """Tests for height setter methods"""
        rectangle_obj1 = Rectangle(3, 10, 0, 0, 10)
        with self.assertRaises(ValueError):
            rectangle_obj1.height = 0
        with self.assertRaises(ValueError):
            rectangle_obj1.height = -4
        with self.assertRaises(TypeError):
            rectangle_obj1.height = True
        rectangle_obj1.height = 3
        self.assertEqual(rectangle_obj1.height, 3)

    def test_height_getter_validations(self):
        """Tests for height getter methods"""
        rectangle_obj1 = Rectangle(3, 4, 0, 0, 10)
        self.assertEqual(rectangle_obj1.height, 4)

    def test_x_setter_validations(self):
        """Tests for x setter methods"""
        rectangle_obj1 = Rectangle(3, 4, 0, 0, 10)
        with self.assertRaises(ValueError):
            rectangle_obj1.x = -1
        with self.assertRaises(TypeError):
            rectangle_obj1.x = [1]
        rectangle_obj1.x = 5
        self.assertEqual(rectangle_obj1.x, 5)

    def test_x_getter_validations(self):
        """Tests for x getter methods"""
        rectangle_obj1 = Rectangle(3, 4, 0, 0, 10)
        self.assertEqual(rectangle_obj1.x, 0)

    def test_y_setter_validations(self):
        """Tests for y setter methods"""
        rectangle_obj1 = Rectangle(3, 4, 0, 0, 10)
        with self.assertRaises(ValueError):
            rectangle_obj1.y = -4
        with self.assertRaises(TypeError):
            rectangle_obj1.y = 'Ho'
        rectangle_obj1.y = 10
        self.assertEqual(rectangle_obj1.y, 10)

    def test_y_getter_validations(self):
        """Tests for y getter methods"""
        rectangle_obj1 = Rectangle(3, 4, 0, 8, 10)
        self.assertEqual(rectangle_obj1.y, 8)

    def test_area_validations(self):
        """Tests for area method"""
        rectangle_obj2 = Rectangle(8, 2, 1, 1, 7)
        self.assertEqual(rectangle_obj2.area(), 16)
        with self.assertRaises(TypeError):
            rectangle_obj2.area(45)
        rectangle_obj2.height = 8
        self.assertEqual(rectangle_obj2.area(), 64)

    def test_display_validations(self):
        """Tests for display method"""
        rectangle_obj3 = Rectangle(3, 2, 1, 1)
        self.assertEqual(rectangle_obj3.display(), None)
        with patch('sys.stdout', new=StringIO()) as get_output:
            rectangle_obj3.display()
            output = '\n ###\n ###\n'
            self.assertEqual(get_output.getvalue(), output)
        with self.assertRaises(TypeError):
            rectangle_obj3.display(True)
        rectangle_obj3.x = 3
        rectangle_obj3.y = 3
        with patch('sys.stdout', new=StringIO()) as get_output:
            rectangle_obj3.display()
            output = '\n\n\n   ###\n   ###\n'
            self.assertEqual(get_output.getvalue(), output)

    def test__str__validations(self):
        """Tests for __str__ method"""
        rectangle_ob4 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(rectangle_ob4.__str__(), '[Rectangle] (12) 2/1 - 4/6')
        rectangle_o5 = Rectangle(2, 3, 4, 5, 8)
        self.assertEqual(rectangle_o5.__str__(), '[Rectangle] (8) 4/5 - 2/3')
        with self.assertRaises(TypeError):
            rectangle_ob4.__str__([2, 4])

    def test_update_validations(self):
        """Tests for update method"""
        rectangle_obj5 = Rectangle(1, 1, 1, 1, 1)
        self.assertEqual(rectangle_obj5.update(), None)
        self.assertEqual(rectangle_obj5.id, 1)
        self.assertEqual(rectangle_obj5.width, 1)
        self.assertEqual(rectangle_obj5.height, 1)
        self.assertEqual(rectangle_obj5.x, 1)
        self.assertEqual(rectangle_obj5.y, 1)
        rectangle_obj5.update(89)
        self.assertEqual(rectangle_obj5.id, 89)
        rectangle_obj5.update(89, 2)
        self.assertEqual(rectangle_obj5.width, 2)
        rectangle_obj5.update(89, 2, 3)
        self.assertEqual(rectangle_obj5.height, 3)
        rectangle_obj5.update(89, 2, 3, 4)
        self.assertEqual(rectangle_obj5.x, 4)
        rectangle_obj5.update(89, 2, 3, 4, 5)
        self.assertEqual(rectangle_obj5.y, 5)
        rectangle_obj5.update(height=1)
        self.assertEqual(rectangle_obj5.height, 1)
        rectangle_obj5.update(width=1, x=2)
        self.assertEqual(rectangle_obj5.width, 1)
        self.assertEqual(rectangle_obj5.x, 2)
        rectangle_obj5.update(y=1, width=2, x=3, id=89)
        self.assertEqual(rectangle_obj5.y, 1)
        self.assertEqual(rectangle_obj5.width, 2)
        self.assertEqual(rectangle_obj5.x, 3)
        self.assertEqual(rectangle_obj5.id, 89)
        rectangle_obj5.update(x=1, height=2, y=3, width=4)
        self.assertEqual(rectangle_obj5.x, 1)
        self.assertEqual(rectangle_obj5.height, 2)
        self.assertEqual(rectangle_obj5.y, 3)
        self.assertEqual(rectangle_obj5.width, 4)
        with self.assertRaises(TypeError):
            rectangle_obj5.update(1, True)
        with self.assertRaises(TypeError):
            rectangle_obj5.update(89, [1])
        with self.assertRaises(ValueError):
            rectangle_obj5.update(89, 2, -3)
        with self.assertRaises(TypeError):
            rectangle_obj5.update(89, 2, 3, 5.5)
        rectangle_obj5.update(89, 2, 3, width=9, height=8)
        self.assertEqual(rectangle_obj5.id, 89)
        self.assertEqual(rectangle_obj5.width, 2)
        self.assertEqual(rectangle_obj5.height, 3)
        with self.assertRaises(TypeError):
            rectangle_obj5.update(height=True)
        rectangle_obj5.update(width=9, height=8)
        self.assertEqual(rectangle_obj5.width, 9)
        self.assertEqual(rectangle_obj5.height, 8)

    def test_to_dictionary_validations(self):
        """Tests for to_dictionary method"""
        rectangle_obj6 = Rectangle(4, 2, 1, 1, 5)
        self.assertEqual(type(rectangle_obj6.to_dictionary()), dict)
        aux = {'id': 5, 'height': 2, 'width': 4, 'x': 1, 'y': 1}
        self.assertTrue(rectangle_obj6.to_dictionary() == aux)
        aux['id'] = 9
        self.assertFalse(rectangle_obj6.to_dictionary() == aux)
        with self.assertRaises(TypeError):
            rectangle_obj6.to_dictionary(89, True, 3, 5.5)

if __name__ == '__main__':
    unittest.main()
