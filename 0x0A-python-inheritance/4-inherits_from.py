#!/usr/bin/python3
"""  Module for function inherits_from  """


def inherits_from(obj, a_class):
    """inherits_from: function that returns True if the object is an instance
        of a class that inherited (directly or indirectly) from the specified
        class; otherwise False
        Args:
            obj (strin): The object to operate
            a_class (class): The class to compare
    """
    res = False
    if type(obj) != a_class:
        res = issubclass(obj.__class__, a_class)
    return res
