#!/usr/bin/python3
"""  Module for function save_to_json_file  """
import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file: function that writes an Object to a text file, using
        a JSON representation
    """
    if filename:
        with open(filename, mode='w', encoding='utf-8') as rfile:
            json.dump(my_obj, rfile)
