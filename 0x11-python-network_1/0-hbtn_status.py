#!/usr/bin/python3
"""Fetch to a page module """
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        page = response.read()
        info = response.info()
        type_of = "\t- type: {}".format(type(page))
        content_of = "\t- content: {}".format(page)
        utf_content_of = "\t- utf8 content: {}".format(str(page, "utf-8"))
        print("Body response:\n{}\n{}\n{}".format(type_of,
                                                  content_of,
                                                  utf_content_of))
