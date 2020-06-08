#!/usr/bin/python3
"""Module for Rectangle Class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class
        Attributes:
            id (int): the id of the rectangle object.
            __width (int): The width of the rectangle object.
            __height (int): The height of the rectangle object.
            __x (int): The x of the rectangle object.
            __y (int): The y of the rectangle object.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__: method that initialize an object"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def to_dictionary(self):
        """to_dictionary: method that returns the dictionary representation of
            a Rectangle
        Return:
            The return value: The rectangle's dictionary
        """
        new_dict = {'id': self.id, 'width': self.width, 'height': self.height,
                    'x': self.x, 'y': self.y}
        return new_dict

    def area(self):
        """area: method that returns the area of the rectangle object
        Return:
            The return value: The rectangle's area
        """
        return self.width * self.height

    def display(self):
        """display: method that returns the prints in stdout the Rectangle
            instance with the character #
        """
        for new_line in range(self.y):
            print('')
        for row in range(self.height):
            for space in range(self.x):
                print(' ', end='')
            for col in range(self.width):
                print('#', end="")
            print('')

    def update(self, *args, **kwargs):
        """update: method that updates the object's attributes
        Args:
            args (tuple or list): new values to update the object
            kwargs (dictionary): new values to update the object
        """
        attributes = ['id', 'width', 'height', 'x', 'y']
        if args and type(args) in [tuple, list]:
            length = len(attributes)
            size = length if len(args) >= length else len(args)
            for index in range(size):
                setattr(self, attributes[index], args[index])
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    if key in attributes:
                        setattr(self, key, value)

    @property
    def width(self):
        """width: getter method for the width attribute
        Return:
            The return value: The rectangle's width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width: setter method for the width attribute
        Args:
            value (int): The width of the rectangle object to modify.
        Raises:
            TypeError: if value is not an integer
            ValueError: If value is less or equal than 0
        """
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """height: getter method for the height attribute
        Return:
            The return value: The rectangle's height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height: setter method for the height attribute
        Args:
            value (int): The height of the rectangle object to modify.
        Raises:
            TypeError: if value is not an integer
            ValueError: If value is less or equal than 0
        """
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """x: getter method for the x attribute
        Return:
            The return value: The rectangle's x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """x: setter method for the x attribute
        Args:
            x (int): The x of the rectangle object to modify.
        Raises:
            TypeError: if value is not an integer
            ValueError: If value is less than 0
        """
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """y: getter method for the y attribute
        Return:
            The return value: The rectangle's y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """y: setter method for the y attribute
        Args:
            y (int): The y of the rectangle object to modify.
        Raises:
            TypeError: if value is not an integer
            ValueError: If value is less than 0
        """
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def __str__(self):
        """__str__: method that converts the rectangle in a string
        Return:
            The return value: The rectangle object in string
        """
        return ('[Rectangle] (' + str(self.id) + ') ' + str(self.x) + '/' +
                str(self.y) + ' - ' + str(self.width) + '/' + str(self.height))
