#!/usr/bin/python3
"""Module for Base Class"""
import json


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
        Args:
            dictionary: double pointer to a dictionary to update an object
        Return:
            The new instance with the attributes set
        """
        if dictionary and type(dictionary) == dict:
            new_object = cls(1, 1, 1, 1)
            new_object.update(**dictionary)
            return new_object

    @classmethod
    def load_from_file(cls):
        """save_to_file: class method that returns a list of instances
        Return:
            A list of instances
        """
        filename = cls.__name__ + '.json'
        try:
            with open(filename, mode='r', encoding='utf-8') as r_file:
                content = r_file.read()
                list_of_dict = cls.from_json_string(content)
                if list_of_dict is None or len(list_of_dict) == 0:
                    return []
                else:
                    if all(type(obj) == dict for obj in list_of_dict):
                        list_of_ins = [cls.create(**item) for item in
                                       list_of_dict]
                        return list_of_ins
                    return []
        except Exception:
            return []

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file: class method that writes the JSON string
            representation of list_objs to a file
        Args:
            list_objs: list of objects who inherits of Base
        """
        value = None
        if list_objs is None:
            value = []
        elif type(list_objs) == list and all(issubclass(type(a), Base) for a in
                                             list_objs):
            value = [obj.to_dictionary() for obj in list_objs]
        if value is not None:
            filename = cls.__name__ + '.json'
            with open(filename, mode='w', encoding='utf-8') as r_file:
                r_file.write(cls.to_json_string(value))

    @classmethod
    def load_from_file_csv(cls):
        """save_to_file: class method that returns a list of instances
        Return:
            A list of instances
        """
        filename = cls.__name__ + '.csv'
        list_of_objs = []
        try:
            with open(filename, mode='r', encoding='utf-8') as r_file:
                for line in r_file:
                    words = line.split(sep=',')
                    new_obj = None
                    if len(words) == 5:
                        new_obj = cls(int(words[1]), int(words[2]),
                                      int(words[3]), int(words[4]),
                                      int(words[0]))
                    if len(words) == 4:
                        new_obj = cls(int(words[1]), int(words[2]),
                                      int(words[3]), int(words[0]))
                    if new_obj is not None:
                        list_of_objs.append(new_obj)
            return list_of_objs
        except Exception:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save_to_file: class method that writes the JSON string
            representation of list_objs to a csv file
        Args:
            list_objs: list of objects who inherits of Base
        """
        value = None
        if type(list_objs) == list and all(issubclass(type(a), Base) for a in
                                           list_objs):
            value = ""
            for obj in list_objs:
                if cls.__name__ == 'Rectangle':
                    value += (str(obj.id) + ',' + str(obj.width) + ',' +
                              str(obj.height) + ',' + str(obj.x) + ',' +
                              str(obj.y) + '\n')
                if cls.__name__ == 'Square':
                    value += (str(obj.id) + ',' + str(obj.size) + ',' +
                              str(obj.x) + ',' + str(obj.y) + '\n')
        if value is not None:
            filename = cls.__name__ + '.csv'
            with open(filename, mode='w', encoding='utf-8') as r_file:
                r_file.write(value)

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string: static method that returns the JSON string
            representation of list_dictionaries
        Args:
            list_dictionaries: list of dictionaries containing data
            representation
        """
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """from_json_string: static method that returns the list of the JSON
            string representation
        Args:
            json_string: string representing a list of dictionaries
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
            except Exception:
                return None
