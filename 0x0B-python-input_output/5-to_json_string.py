#!/usr/bin/python3
"""  Module for function to_json_string  """
import json


def to_json_string(my_obj):
    """to_json_string: function that returns the JSON representation of an
        object (string)
    """
    if my_obj:
        return json.dumps(my_obj)
