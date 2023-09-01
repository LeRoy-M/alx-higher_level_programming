#!/usr/bin/python3
"""Module that displays value of 'X-Request-Id' variable found in the
header of the URL response
"""
import urllib.request as UR
from sys import argv

if __name__ == "__main__":
    with UR.urlopen(argv[1]) as response:
        print(dict(response.headers)["X-Request-Id"])
