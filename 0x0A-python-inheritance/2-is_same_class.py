#!/usr/bin/python3
"""  Module for function is_same_class  """


def is_same_class(obj, a_class):
    """is_same_class: function that returns True if the object is exaclty an
        instance of the specified class; otherwise False
        Args:
            obj (strin): The object to operate
            a_class (class): The class to compare
    """
    return (obj.__class__ == a_class)
