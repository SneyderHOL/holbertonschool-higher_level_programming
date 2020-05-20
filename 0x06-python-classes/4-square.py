#!/usr/bin/python3
"""  Square Class  """


class Square:
    """__init__: method to initilize object's properties.

    Args:
        size (int): The size of the square object to initialize.

    Attributes:
        __size (int): The size of the square object.

    Raises:
        TypeError: if size is not an integer
        ValueError: If size is less than 0

    """
    def __init__(self, size=0):
        self.size = size

    """area: method to calculate the area of the square object

    Attributes:
        __size (int): The size of the square object.

    Return:
        The return value: The square size to the power 2

    """
    def area(self):
        return self.__size ** 2

    """size: method to get the size attribute

    Attributes:
        __size (int): The size of the square object.

    Return:
        The return value: The square size

    """
    @property
    def size(self):
        return self.__size

    """size: method to modify the size attribute

    Args:
        value (int): The size of the square object to modify.

    Attributes:
        __size (int): The size of the square object.

    Raises:
        TypeError: if size is not an integer
        ValueError: If size is less than 0

    """
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
