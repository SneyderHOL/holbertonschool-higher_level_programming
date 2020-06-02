#!/usr/bin/python3
"""  Module for function lookup  """


def lookup(obj):
    """lookup: function that returns the list of available attributes and
        methods of an object
    """
    return list(dir(obj))
