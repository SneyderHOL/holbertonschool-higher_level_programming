#!/usr/bin/python3
"""Fetch to a page module """
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        page = response.read()
        info = response.info()
        print(info.get("X-Request-Id"))
