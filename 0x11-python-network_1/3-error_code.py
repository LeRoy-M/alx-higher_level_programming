#!/usr/bin/python3
"""Module that takes a URL and displays the body of the response"""
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from sys import argv

if __name__ == "__main__":
    request = Request(argv[1])

    try:
        with urlopen(request) as response:
            print(response.read().decode("utf-8"))
    except HTTPError as e:
        print(f"Error code: {e.code}")
