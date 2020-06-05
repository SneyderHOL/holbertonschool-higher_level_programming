#!/usr/bin/python3
"""  Module for function append_after  """


def append_after(filename="", search_string="", new_string=""):
    """append_after: function that inserts a line of text to a file, after each
        line containing a specific string
    """
    if filename:
        with open(filename, mode='r+', encoding='utf-8') as readfile:
            content = readfile.readlines()
            readfile.seek(0)
            for line in content:
                readfile.write(line)
                if search_string in line:
                    readfile.write(new_string)
