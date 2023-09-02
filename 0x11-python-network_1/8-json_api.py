#!/usr/bin/python3
"""Module that takes a letter and sends a 'POST' request to
'http://0.0.0.0:5000/search_user' with the letter as
a parameter
"""
import requests
from sys import argv

if __name__ == "__main__":
    q = ""
    if len(argv) > 1:
        q = argv[1]
    response = requests.get("http://0.0.0.0:5000/search_user", {"q": q})
    print(response.text)
