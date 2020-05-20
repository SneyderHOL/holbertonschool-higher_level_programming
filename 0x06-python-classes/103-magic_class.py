#!/usr/bin/python3

"""  MagicClass Class
    Attributes:
        _MagicClass__radius (int): The radius of a circle.
"""
import math


class MagicClass:
    """  MagicClass Class
        Attributes:
            _MagicClass__radius (int): The radius of a circle.
    """

    def __init__(self, radius=0):
        """__init__: method to initilize object's properties.

        Args:
            radius (int or float): The radius of the object to initialize.

        Raises:
            TypeError: if radius is not an integer or if is not a float

        """
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """area: method to calculate the area of a circle object

        Return:
            The return value: The object radius to the power 2 times pi

        """
        return (self._MagicClass__radius ** 2) * math.pi

    def circumference(self):
        """circumference: calculate the circumference of a circle object

        Return:
            The return value: The object radius times 2 times pi

        """
        return (2 * math.pi) * self._MagicClass__radius
