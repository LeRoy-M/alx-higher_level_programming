#!/usr/bin/python3
"""Module that displays value of 'X-Request-Id' variable found in the
header of the URL response
"""
import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[1])
    print(response.headers["X-Request-Id"])
