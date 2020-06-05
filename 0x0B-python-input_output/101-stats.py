#!/usr/bin/python3
"""  Script stats  """
import sys
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
cycle = 10


def print_info():
    print('File size: {:d}'.format(total_size))
    for code in sorted(status_codes):
        if status_codes.get(code) != 0:
            print('{:d}: {}'.format(code, status_codes[code]))

try:
    for line in sys.stdin:
        if cycle == 0:
            cycle = 10
            print_info()
        tokens = line.split()
        total_size += int(tokens[8])
        cod = int(tokens[7])
        status_codes[cod] = status_codes.get(cod) + 1
        cycle -= 1
finally:
    print_info()
