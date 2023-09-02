#!/usr/bin/python3
"""Module that takes a URL and an email, sends a 'POST' request to the URL
with the email as a parameter, and displays the body of the response
"""
import requests
from sys import argv

if __name__ == "__main__":
    payload = {"email": argv[2]}
    response = requests.get(argv[1])
    print(response.url())
