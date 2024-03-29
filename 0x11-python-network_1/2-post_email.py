#!/usr/bin/python3
"""Module that takes a URL and an email, sends a 'POST' request to the URL
with the email as a parameter, and displays the body of the response
"""
import urllib.request as UR
import urllib.parse as UP
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    val = {"email": argv[2]}
    data = UP.urlencode(val).encode("ascii")
    request = UR.Request(url, data)

    with UR.urlopen(request) as response:
        print(response.read().decode("utf-8"))
