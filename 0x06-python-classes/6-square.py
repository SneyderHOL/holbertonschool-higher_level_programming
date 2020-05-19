#!/usr/bin/python3
"""  Square Class  """


class Square:
    """__init__: method to initilize object's properties.

    Args:
        size (int): The size of the square object to initialize.
        position (tuple): The position of the square object to initialize.

    Attributes:
        __size (int): The size of the square object.
        __position (tuple): The position of the square object.

    Raises:
        TypeError: if size is not an integer or if position is not a tuple
        ValueError: If size is less than 0

    """
    def __init__(self, size=0, position=(0, 0)):
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        elif (type(position) != tuple or len(position) != 2 or
              position[0] < 0 or position[1] < 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__size = size
        self.__position = position

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

    """size: method to get the size attribute

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

    """my_print: method that prints in stdout the square with the character #,
        if size is equal to 0, print an empty ine

    Attributes:
        __size (int): The size of the square object.
        __position (tuple): The position of the square object.

    """
    def my_print(self):
        if self.__size > 0:
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print('_', end="")
                for k in range(self.__size):
                    print('#', end="")
                print('')
        else:
            print('')

    """position: method to get the position attribute

    Attributes:
        __position (tuple): The position of the square object.

    Return:
        The return value: The square position

    """
    @property
    def position(self):
        return self.__position

    """position: method to modify the position attribute

    Args:
        value (tuple): The position of the square object to modify.

    Attributes:
        __position (tuple): The position of the square object.

    Raises:
        TypeError: if value is not a tuple or does not contain positive
        integers

    """
    @position.setter
    def position(self, value):
        if (type(value) != tuple or len(value) != 2 or value[0] < 0 or
                value[1] < 0):
            raise TypeError('value must be a tuple of 2 positive integers')
        self.__position = value
