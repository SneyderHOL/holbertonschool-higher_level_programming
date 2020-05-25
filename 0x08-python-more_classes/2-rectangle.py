#!/usr/bin/python3
class Rectangle:
    """Rectangle Class"""

    def __init__(self, width=0, height=0):
        """__init__: method to initilize object's properties.
        Args:
            width (int): The width of the rectangle object to initialize.
            height (int): The height of the rectangle object to initialize.
        Attributes:
            __width (int): The width of the rectangle object.
            __height (int): The height of the rectangle object.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """width: getter method for the width attribute
        Attributes:
            __width (int): The width of the rectangle object.
        Return:
            The return value: The rectangle width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width: setter method for the width attribute
        Args:
            value (int): The width of the rectangle object to modify.
        Attributes:
            __width (int): The width of the rectangle object.
        Raises:
            TypeError: if value is not an integer
            ValueError: If value is less than 0
        """
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """height: getter method for the height attribute
        Attributes:
            __height (int): The height of the rectangle object.
        Return:
            The return value: The rectangle height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height: setter method for the height attribute
        Args:
            value (int): The height of the rectangle object to modify.
        Attributes:
            __height (int): The height of the rectangle object.
        Raises:
            TypeError: if value is not an integer
            ValueError: If value is less than 0
        """
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """area: method to calculate the area of the rectangle object
            Attributes:
            __width (int): The width of the rectangle object.
            __height (int): The height of the rectangle object.
        Return:
            The return value: The rectangle's area
        """
        return self.width * self.height

    def perimeter(self):
        """perimeter: method to calculate the perimeter of the rectangle object
            Attributes:
            __width (int): The width of the rectangle object.
            __height (int): The height of the rectangle object.
        Return:
            The return value: The rectangle's perimeter
        """
        if self.width != 0 and self.height != 0:
            return (self.width * 2) + (self.height * 2)
        return 0
