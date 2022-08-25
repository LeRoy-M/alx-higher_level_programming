#!/usr/bin/python3
from sys import argv

if __name__ != "__main__":
    exit()

argc = len(argv) - 1

if argc == 0:
    print(f"{argc} arguments.")
elif argc == 1:
    print(f"{argc} argument:")
    print(f"{argc}: {argv[argc]}")
elif argc > 0:
    print(f"{argc} arguments:")
    i = 0
    while i != argc:
        print(f"{i + 1}: {argv[i + 1]}")
        i += 1
