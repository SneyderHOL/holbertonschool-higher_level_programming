#!/usr/bin/python3
"""Unittest for Base"""
import unittest
import json
from models import base
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Class for testing with unit test the Base class"""

    def test_docstrings(self):
        """Tests for dosctrings"""
        self.assertGreater(len(base.__doc__), 1)
        self.assertGreater(len(Base.__doc__), 1)
        self.assertGreater(len(Base.__init__.__doc__), 1)
        self.assertGreater(len(Base.save_to_file.__doc__), 1)
        self.assertGreater(len(Base.load_from_file.__doc__), 1)
        self.assertGreater(len(Base.save_to_file_csv.__doc__), 1)
        self.assertGreater(len(Base.load_from_file_csv.__doc__), 1)
        self.assertGreater(len(Base.to_json_string.__doc__), 1)
        self.assertGreater(len(Base.from_json_string.__doc__), 1)
        self.assertGreater(len(Base.create.__doc__), 1)

    def test_new_object(self):
        """Tests when an instance is created"""
        base_obj = Base()
        self.assertIsInstance(base_obj, Base)
        self.assertEqual(base_obj.id, 1)
        base_obj2 = Base(9)
        self.assertEqual(base_obj2.id, 9)
        base_obj3 = Base('a')
        self.assertEqual(base_obj3.id, 'a')
        base_obj4 = Base()
        self.assertEqual(base_obj4.id, 2)
        with self.assertRaises(TypeError):
            base_obj5 = Base(1, 3)

    def test_save_to_file(self):
        """Tests for save_to_file method"""
        rectangle_obj = Rectangle(9, 8, 1, 2, 23)
        square_obj = Square(4, 5, 6, 21)
        Base.save_to_file([rectangle_obj, square_obj])
        with open('Base.json', mode='r', encoding='utf-8') as n_file:
            f_cont = json.load(n_file)
            self.assertEqual(type(f_cont), list)
            self.assertEqual(len(f_cont), 2)
        with self.assertRaises(TypeError):
            Base.save_to_file()

    def test_load_from_file(self):
        """Tests for load_from_file method"""
        pass

    def test_to_json_string(self):
        """Tests for to_json_string method"""
        res = Base.to_json_string([])
        self.assertEqual(type(res), str)
        self.assertEqual(Base.to_json_string(None), '[]')
        self.assertEqual(Base.to_json_string(1), '1')
        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.to_json_string([{}]), '[{}]')
        self.assertEqual(Base.to_json_string([1]), '[1]')
        self.assertEqual(Base.to_json_string([[1, 2]]), '[[1, 2]]')
        self.assertEqual(Base.to_json_string([(True, 2)]), '[[true, 2]]')
        self.assertEqual(Base.to_json_string([{'id': 3}]), '[{"id": 3}]')
        with self.assertRaises(TypeError):
            Base.to_json_string()
        with self.assertRaises(TypeError):
            Base.to_json_string([], [])

    def test_from_json_string(self):
        """Tests for from_json_string method"""
        with self.assertRaises(TypeError):
            Base.from_json_string()
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(''), [])
        self.assertEqual(Base.from_json_string('[]'), [])
        self.assertEqual(Base.from_json_string(1), None)
        self.assertEqual(Base.from_json_string((1, 2)), None)
        self.assertEqual(Base.from_json_string(True), None)
        self.assertEqual(Base.from_json_string('[{}]'), [{}])
        self.assertEqual(Base.from_json_string('[{"id": 3}]'), [{'id': 3}])

    def test_create(self):
        """Tests for create method"""
        pass

if __name__ == '__main__':
    unittest.main()
