#!/usr/bin/python3
"""Module for clase Rectangle"""


class Rectangle:
    """Rectangle Class
        Attributes:
            number_of_instances (int): The number of rectangle objects
    """

    number_of_instances = 0
    print_symbol = '#'

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
        type(self).number_of_instances += 1

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

    def __str__(self):
        """__str__: method that converts the rectangle in a string
        Return:
            The return value: The rectangle object in string
        """
        str_rec = ''
        for i in range(self.height):
            for j in range(self.width):
                str_rec += str(self.print_symbol)
            if i != self.height - 1:
                str_rec += '\n'
        return str_rec

    def __repr__(self):
        """__repr__: method that makes the representation of a
            rectangle in a string
        Return:
            The return value: The rectangle object representation
            in string
        """
        return 'Rectangle (' + str(self.width) + ', ' + str(self.height) + ')'

    def __del__(self):
        """__del__: method that is executed when a rectangle object is deleted
        """
        if type(self).number_of_instances > 0:
            type(self).number_of_instances -= 1
            print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """bigger_or_equal: method that returns the biggest rectangle based on
            the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """square: method that returns a new Rectangle instance based with
            width == height == size
        """
        return cls(size, size)
