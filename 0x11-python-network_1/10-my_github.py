#!/usr/bin/python3
"""Fetch to a page module """
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    url = "https://api.github.com/user"
    user = sys.argv[1]
    u_pass = sys.argv[2]
    req = requests.get(url, auth=HTTPBasicAuth(user, u_pass))
    try:
        result = req.json()
        if result == {}:
            print('None')
        else:
            print('{}'.format(result.get('id')))
    except ValueError as e:
        print('Not a valid JSON')
