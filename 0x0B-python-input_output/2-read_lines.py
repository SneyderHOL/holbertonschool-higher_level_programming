#!/usr/bin/python3
"""  Module for function read_lines  """


def read_lines(filename="", nb_lines=0):
    """read_lines: function that reads n lines of a text file (UTF8) and prints
         it to stdout
    """
    if filename:
        with open(filename, encoding='utf-8') as readfile:
            if nb_lines <= 0 or nb_lines >= len(readfile.readlines()):
                readfile.seek(0)
                print(readfile.read(), end='')
            else:
                i = 0
                readfile.seek(0)
                while i < nb_lines:
                    print(readfile.readline(), end='')
                    i += 1
