#!/usr/bin/python3
"""  Module for function read_file  """


def read_file(filename=""):
    """read_file: function that reads a text file (UTF8) and prints it to
        stdout
    """
    if filename:
        with open(filename, encoding='utf-8') as readfile:
            print(readfile.read(), end='')
