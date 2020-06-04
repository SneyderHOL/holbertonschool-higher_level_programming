#!/usr/bin/python3
"""  Script add_item  """
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


def add_item(obj):
    """lookup: function that returns the list of available attributes and
        methods of an object
    """
    return list(dir(obj))

if __name__ == '__main__':
    filename = 'add_item.json'
    n_list = []
    size = len(sys.argv) - 1
    if size > 0:
        n_list = load_from_json_file(filename)
        i = 0
        while i < size:
            n_list.append(sys.argv[i + 1])
            i += 1
        save_to_json_file(n_list, filename)
    else:
        save_to_json_file(n_list, filename)
