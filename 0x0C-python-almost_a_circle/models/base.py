#!/usr/bin/python3
"""Module for Base Class"""
import json
from models.rectangle import Rectangle
from models.square import Square


class Base:
    """Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """__init__: method that initialize an object"""
        if id is None:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @classmethod
    def create(cls, **dictionary):
        """create: class method that returns an instance with all attributes
            already set
        """
        if dictionary and type(dictionary) == dict:
            new_object = None
            if 'size' in dictionary:
                new_object = Square(1, 1, 1, 1)
            elif 'width' in dictionary:
                new_object = Rectangle(1, 1, 1, 1, 1)
            if new_object is not None:
                new_object.update(dictionary)
            return new_object

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file: class method that writes the JSON string
            representation of list_objs to a file
        """
        value = None
        if list_objs is None:
            value = []
        elif type(list_objs) == list and all(issubclass(type(a), Base) for a in
                                             list_objs):
            value = [obj.to_dictionary() for obj in list_objs]
        if value is not None:
            str_file = cls.__name__ + '.json'
            with open(str_file, mode='w', encoding='utf-8') as r_file:
                r_file.write(cls.to_json_string(value))

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string: static method that returns the JSON string
            representation of list_dictionaries
        """
        if list_dictionaries is None:
            return '[]'
        if type(list_dictionaries) == list:
            if len(list_dictionaries) == 0:
                return '[]'
            if all(type(a) == dict for a in list_dictionaries):
                return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """from_json_string: static method that returns the list of the JSON
            string representation
        Return:
            The list of the JSON string representation
        """
        list_of_objs = []
        if json_string is None:
            return list_of_objs
        if type(json_string) == str:
            if len(json_string) == 0:
                return list_of_objs
            try:
                list_of_objs = json.loads(json_string)
                if type(list_of_objs) == list:
                    if len(list_of_objs) == 0:
                        return list_of_objs
                    if all(type(obj) == dict for obj in list_of_objs):
                        return list_of_objs
            except:
                return None
