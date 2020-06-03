#!/usr/bin/python3
"""  Module for function number_of_lines  """


def number_of_lines(filename=""):
    """number_of_lines: function that returns the number of lines of a text
        file
    """
    if filename:
        with open(filename, encoding='utf-8') as readfile:
            return len(readfile.readlines())
