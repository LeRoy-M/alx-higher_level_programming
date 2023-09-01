#!/usr/bin/python3
"""Module that fetches 'https://alx-intranet.hbtn.io/status'"""
import urllib.request as UR

if __name__ == "__main__":
    with UR.urlopen("https://alx-intranet.hbtn.io/status") as response:
        body = response.read()
        print(body)
