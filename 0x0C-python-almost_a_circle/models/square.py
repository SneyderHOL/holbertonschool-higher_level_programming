#!/usr/bin/python3
"""Module for Square Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """__init__: method that initialize an object"""
        super().__init__(size, size, x, y, id)

    def to_dictionary(self):
        """to_dictionary: method that returns the dictionary representation of
            a Square
        Return:
            The return value: The square's dictionary
        """
        new_dict = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return new_dict

    def update(self, *args, **kwargs):
        """update: method that updates the object's attributes
        Args:
            args (tuple or list): new values to update the object
            kwargs (dictionary): new values to update the object
        """
        attributes = ['id', 'size', 'x', 'y']
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
    def size(self):
        """size: getter method for the size of the square object that could be
            width or height attribute
        Return:
            The return value: The square's size
        """
        return self.width

    @size.setter
    def size(self, value):
        """size: setter method for the width and height attribute
        Args:
            value (int): The width and height of the square object to modify.
        Raises:
            TypeError: if value is not an integer
            ValueError: If value is less or equal than 0
        """
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.width = value
        self.height = value

    def __str__(self):
        """__str__: method that converts the square in a string
        Return:
            The return value: The square object in string
        """
        return ('[Square] (' + str(self.id) + ') ' + str(self.x) + '/' +
                str(self.y) + ' - ' + str(self.width))
