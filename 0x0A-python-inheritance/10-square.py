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
        super().__init__(size, size)
        self.__size = size
