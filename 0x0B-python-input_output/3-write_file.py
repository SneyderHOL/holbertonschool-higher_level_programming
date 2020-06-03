#!/usr/bin/python3
"""  Module for function write_file  """


def write_file(filename="", text=""):
    """write_file: function that writes a string to a text file (UTF8) and
        returns the number of characters written
    """
    if filename:
        with open(filename, mode='w', encoding='utf-8') as readfile:
            return readfile.write(text)
