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
        request_id = info.get_params(header="X-Request-Id")
        if len(request_id) > 0:
            print(request_id[0][0])
