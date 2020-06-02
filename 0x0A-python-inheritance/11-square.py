#!/usr/bin/python3
"""  Module for Square Class  """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """  Module for Square Class  """

    def __init__(self, size):
        """__init__: method to initilize object's properties.
        Args:
            size (int): The size of the square object to initialize.
        Attributes:
            __size (int): The size of the square object.
        """
        self.integer_validator('size', size)
        self.__width = size
        self.__height = size
        self.__size = size

    def area(self):
        """area: method that returns the area of the square object
        Return:
            The return value: The square's area
        """
        return self.__width * self.__height

    def __str__(self):
        """__str__: method that converts the square in a string
        Return:
            The return value: The square object in string
        """
        return '[Square] ' + str(self.__width) + '/' + str(self.__height)
