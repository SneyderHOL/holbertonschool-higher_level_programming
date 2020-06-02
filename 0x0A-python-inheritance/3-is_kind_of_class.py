#!/usr/bin/python3
"""  Module for function is_kind_of_class  """


def is_kind_of_class(obj, a_class):
    """is_kind_of_class: function that returns True if the object is an
        instance of, or if the object is an instance of a class that inherited
        from, the specified class; otherwise False
        Args:
            obj (strin): The object to operate
            a_class (class): The class to compare
    """
    return isinstance(obj, a_class)
