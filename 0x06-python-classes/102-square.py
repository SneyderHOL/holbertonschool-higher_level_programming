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

    """__eq__: method to calculate if two objects are equal

    Attributes:
        other (object): object to compare

    Return:
        The return value: True if the two objects are equal, False if not

    """
    def __eq__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        return self.size == other.size

    """__ne__: method to calculate if two objects are not equal

    Attributes:
        other (object): object to compare

    Return:
        The return value: True if the two objects are not equal, False if not

    """
    def __ne__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        return self.size != other.size

    """__ge__: method to calculate if one object are greater or equal than
        other

    Attributes:
        other (object): object to compare

    Return:
        The return value: True if the the objects are equal or greater than
        other, or False if not

    """
    def __ge__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        return self.size >= other.size

    """__le__: method to calculate if one object are less or equal than other

    Attributes:
        other (object): object to compare

    Return:
        The return value: True if one objects are less or equal than other, or
        False if not

    """
    def __le__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        return self.size <= other.size

    """__gt__: method to calculate if one object are greater than other

    Attributes:
        other (object): object to compare

    Return:
        The return value: True if one object are greater than other, or False
        if not

    """
    def __gt__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        return self.size > other.size

    """__lt__: method to calculate if one objects is less than other

    Attributes:
        other (object): object to compare

    Return:
        The return value: True if one object is less than other, or False if
        not

    """
    def __lt__(self, other):
        if not isinstance(other, Square):
            return NotImplemented
        return self.size < other.size
