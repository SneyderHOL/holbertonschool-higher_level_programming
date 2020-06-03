#!/usr/bin/python3
"""  Module for function add_attribute  """


def add_attribute(obj, name, value):
    """add_attribute: function that adds a new attribute to an object if it's
        posible
    """
    if '__dict__' in dir(obj):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
