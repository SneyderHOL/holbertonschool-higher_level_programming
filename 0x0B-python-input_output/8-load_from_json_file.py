#!/usr/bin/python3
"""  Module for function load_from_json_file  """
import json


def load_from_json_file(filename):
    """load_from_file: function that creates an Object from a "JSON file"
    """
    if filename:
        with open(filename, encoding='utf-8') as rfile:
            return json.load(rfile)
