#!/usr/bin/python3
"""Fetch to a page module """
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    code = req.status_code
    if code >= 400:
        print("Error code: {}".format(code))
    else:
        print(req.text)
