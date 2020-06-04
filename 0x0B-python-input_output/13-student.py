#!/usr/bin/python3
"""  Module for Student Class  """


class Student:
    """  Student class """
    def __init__(self, first_name, last_name, age):
        """__init__: function to initialize the student object
        Args:
            first_name (string): first name attribute for the student object
            last_name (string): last name attribute for the student object
            age (int): name attribute for the student object
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to_json: method that retrieves a dictionary representation of a
            Student instance
        Args:
            attrs (list): list of strings
        """
        if attrs is not None:
            ret_dict = {}
            for a in attrs:
                if type(a) == str:
                    if a in self.__dict__:
                        ret_dict[a] = self.__dict__.get(a)
                else:
                    return self.__dict__
            return ret_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """reload_from_json: method that replace all attributes of the Student
            instance
        Args:
            json (dict): dictionary
        """
        if json:
            for k, v in json.items():
                self.__dict__[k] = v
