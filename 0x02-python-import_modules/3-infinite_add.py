#!/usr/bin/python3
from sys import argv

if __name__ != "__main__":
    exit()

argc = len(argv) - 1

i = 1
total = 0
if argc == 0:
    print(f"{total}")
if argc > 0:
    while i != argc:
        total += eval(argv[i])
        i += 1
    print(f"{total + eval(argv[i])}")
