#!/usr/bin/python3
"""  Module for BaseGeometry Class  """


class BaseGeometry:
    """  BaseGeometry class """

    def area(self):
        """area: method that raises an Exception with the message area() is not
            implemented
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """integer_validator: method that validates the argument value"""
        if type(value) != int:
            raise TypeError(name + ' must be an integer')
        if value <= 0:
            raise ValueError(name + ' must be greater than 0')
