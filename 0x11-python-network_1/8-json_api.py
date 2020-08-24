#!/usr/bin/python3
"""Fetch to a page module """
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    user = ""
    if len(sys.argv) > 1:
        user = sys.argv[1]
    data = {'q': user}
    req = requests.post(url, data)
    try:
        result = req.json()
        if result == {}:
            print('No result')
        else:
            print('[{}] {}'.format(result.get('id'), result.get('name')))
    except ValueError as e:
        print('Not a valid JSON')
