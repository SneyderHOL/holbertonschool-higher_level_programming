#!/usr/bin/python3
"""Fetch to a page module """
import requests


if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    req = requests.get(url)
    page = req.text
    type_of = "\t- type: {}".format(type(page))
    content_of = "\t- content: {}".format(page)
    print("Body response:\n{}\n{}".format(type_of, content_of))
