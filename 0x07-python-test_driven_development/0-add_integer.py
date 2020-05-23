#!/usr/bin/python3
"""
Module that adds two integers
"""


def add_integer(a, b=98):
    """add_integer is a function that adds 2 integers
    Args:
        a (int): number to operate
        b (int): number to operate
    Raises:
        TypeError: if a or b are not an integer
    """
    if type(a) != int:
        if type(a) == float:
            a = int(a)
        else:
            raise TypeError('a must be an integer')
    if type(b) != int:
        if type(b) == float:
            b = int(b)
        else:
            raise TypeError('b must be an integer')
    return int(a + b)
