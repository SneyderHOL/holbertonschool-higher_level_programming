#!/usr/bin/python3
"""  Module for MyInt Class  """


class MyInt(int):
    """  MyInt class """
    def __eq__(self, other):
        """__eq__: method to calculate if two objects are equal
        Attributes:
            other (object): object to compare
        Return:
            The return value: True if the two objects are equal, False if not
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """__eq__: method to calculate if two objects are not equal
        Attributes:
            other (object): object to compare
        Return:
            The return value: True if the two objects are not equal, False if
            not
        """
        return super().__eq__(other)
