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
    if type(a) != int and type(a) != float:
        raise TypeError('a must be an integer')
    if type(b) != int and type(b) != float:
        raise TypeError('b must be an integer')
    return int(a) + int(b)
