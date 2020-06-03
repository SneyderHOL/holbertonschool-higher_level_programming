#!/usr/bin/python3
"""  Module for function append_write  """


def append_write(filename="", text=""):
    """append_write: function that appends at the end of a text file(UTF8)and
        returns the number of characters added
    """
    if filename:
        with open(filename, mode='a', encoding='utf-8') as readfile:
            return readfile.write(text)
