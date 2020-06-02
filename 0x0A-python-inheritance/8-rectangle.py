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
