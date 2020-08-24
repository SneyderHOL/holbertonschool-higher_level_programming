#!/usr/bin/python3
"""Fetch to a page module """
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    headers = req.headers
    print(headers.get('X-Request-Id'))
