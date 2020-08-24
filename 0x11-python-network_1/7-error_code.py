#!/usr/bin/python3
"""Fetch to a page module """
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    try:
        req.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("Error_code: {}".format(code))
    else:
        print(req.text)
