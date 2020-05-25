#!/usr/bin/python3
"""Module for clase Rectangle"""


class Rectangle:
    """__init__: method to initilize object's properties.
        Args:
            width (int): The width of the rectangle object to initialize.
            height (int): The height of the rectangle object to initialize.
        Attributes:
            __width (int): The width of the rectangle object.
            __height (int): The height of the rectangle object.
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    """width: getter method for the width attribute
        Attributes:
            __width (int): The width of the rectangle object.
        Return:
            The return value: The rectangle width
    """
    @property
    def width(self):
        return self.__width

    """width: setter method for the width attribute
        Args:
            value (int): The width of the rectangle object to modify.
        Attributes:
            __width (int): The width of the rectangle object.
        Raises:
            TypeError: if value is not an integer
            ValueError: If value is less than 0
    """
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    """height: getter method for the height attribute
        Attributes:
            __height (int): The height of the rectangle object.
        Return:
            The return value: The rectangle height
    """
    @property
    def height(self):
        return self.__height

    """height: setter method for the height attribute
        Args:
            value (int): The height of the rectangle object to modify.
        Attributes:
            __height (int): The height of the rectangle object.
        Raises:
            TypeError: if value is not an integer
            ValueError: If value is less than 0
    """
    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
