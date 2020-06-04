#!/usr/bin/python3
"""  Script add_item  """
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = 'add_item.json'
n_list = []
size = len(sys.argv) - 1
if size > 0:
    try:
        n_list = load_from_json_file(filename)
    except Exception:
        n_list = []
    finally:
        i = 0
        while i < size:
            n_list.append(sys.argv[i + 1])
            i += 1
        save_to_json_file(n_list, filename)
else:
    save_to_json_file(n_list, filename)
