#!/usr/bin/python3
"""Module that takes 2 arguments in order to solve provided challenge"""
import requests
from sys import argv

if __name__ == "__main__":
    url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"
    commits = requests.get(url).json()
    count = len(commits) - 1
    for i in range(count, (count - 10), -1):
        print(commits[i])
