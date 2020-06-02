#!/usr/bin/python3
"""  Module for Rectangle Class  """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """  Rectangle class """
    def __init__(self, width, height):
        """__init__: method that initialize an object"""
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """area: method that returns the area of the rectangle object
        Return:
            The return value: The rectangle's area
        """
        return self.__width * self.__height

    def __str__(self):
        """__str__: method that converts the rectangle in a string
        Return:
            The return value: The rectangle object in string
        """
        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)
