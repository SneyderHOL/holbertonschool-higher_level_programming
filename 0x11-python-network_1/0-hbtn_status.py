#!/usr/bin/python3
"""Fetch to a page module """
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        page = response.read()
        info = response.info()
        print('Body response:')
        print('\t - type: {}'.format(type(page)))
        print('\t - content: {}'.format(page))
        print('\t - utf8 content: {}'.format(str(page, "utf-8")))
