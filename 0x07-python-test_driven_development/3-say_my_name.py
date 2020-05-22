#!/usr/bin/python3
"""
Module that prints the name
"""


def say_my_name(first_name, last_name=""):
    """say_my_name is a function that prints My name is <first name> <last
        name>
    Args:
        first_name (string): string to print
        last_name (string): number to print

    Raises:
        TypeError: if first_name or b last_name are not a string
    """
    if type(first_name) != str:
        raise TypeError('first_name must be a string')
    if type(last_name) != str:
        raise TypeError('last_name must be a string')
    print('My name is {} {}'.format(first_name, last_name))
