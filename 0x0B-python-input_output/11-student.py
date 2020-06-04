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

    def to_json(self):
        """to_json: method that retrieves a dictionary representation of a
            Student instance
        """
        return self.__dict__
