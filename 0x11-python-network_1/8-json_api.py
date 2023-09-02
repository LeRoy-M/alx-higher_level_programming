#!/usr/bin/python3
"""Module that takes a letter and sends a 'POST' request to
'http://0.0.0.0:5000/search_user' with the letter as
a parameter
"""
import requests
from sys import argv

if __name__ == "__main__":
    q = "" if len(argv) < 2 else argv[1]

    response = requests.post("http://0.0.0.0:5000/search_user", {"q": q})
    try:
        api = response.json()
        if not api:
            print("No result")
        else:
            print(f"[{api['id']}] {api['name']}")
    # except requests.exceptions.JSONDecodeError:
    except ValueError:
        print("Not a valid JSON")
