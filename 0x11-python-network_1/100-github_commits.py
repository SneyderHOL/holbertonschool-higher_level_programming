#!/usr/bin/python3
"""Fetch to a page module """
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    payload = {'per_page': '10', 'page': '1'}
    req = requests.get(url, params=payload)
    try:
        result = req.json()
        if result == {} or result == []:
            print('None')
        else:
            for res in result:
                sha = res.get('sha')
                author = res.get('commit').get('author').get('name')
                result_str = "{}: {}".format(sha, author)
                print(result_str)
    except ValueError as e:
        print('Not a valid JSON')
