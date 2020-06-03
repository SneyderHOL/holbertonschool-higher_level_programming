#!/usr/bin/python3
"""  Module for function from_json_string  """
import json


def from_json_string(my_str):
    """from_json_string: function that returns an object (Python data
        structure) represented by a JSON string
    """
    return json.loads(my_str)
