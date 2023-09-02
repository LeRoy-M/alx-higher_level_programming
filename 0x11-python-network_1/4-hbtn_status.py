#!/usr/bin/python3
"""Module that fetches 'https://alx-intranet.hbtn.io/status'"""
import requests

if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type:", type(str(response)))
    print("\t- content:", response.content)
