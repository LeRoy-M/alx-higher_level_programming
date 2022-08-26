#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if 97 <= ord(char) <= 122:
            str2 = 32
        else:
            str2 = 0
        print("{}".format(chr(ord(char) - str2)), end='')
    print()
