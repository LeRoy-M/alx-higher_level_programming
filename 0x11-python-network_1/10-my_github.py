#!/usr/bin/python3
"""Module that takes ones GitHub credentials (username & password) and uses
the GitHub API to display their 'id'
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/user"
    api_r = requests.get(url, auth=(argv[1], argv[2])).json()
    print(api_r.get("id"))
