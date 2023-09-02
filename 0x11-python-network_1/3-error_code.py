#!/usr/bin/python3
"""Module that takes a URL and displays the body of the response"""
from urllib import request, error
from sys import argv

if __name__ == "__main__":
    # request = request.Request(argv[1])

    # with request.urlopen(request) as response:
    with request.urlopen(argv[1]) as response:
        try:
            print(response.read().decode("utf-8"))
        except error.HTTPError as e:
            print(f"Error code: {e.code}")
