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
        if info.get_content_charset() == 'utf-8':
            print('\t - utf8 content: OK')
