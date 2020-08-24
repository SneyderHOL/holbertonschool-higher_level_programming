#!/usr/bin/python3
"""Fetch to a page module """
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(req) as response:
            page = response.read()
            content = str(page, "utf-8")
            print(content)
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
