#!/usr/bin/python3
"""Module that takes a URL and an email, sends a 'POST' request to the URL
with the email as a parameter, and displays the body of the response
"""
import urllib.request as UR
from sys import argv

if __name__ == "__main__":
    with UR.urlopen(f"argv[1]?email=argv[2]") as response:
        print(reponse)
