#!/usr/bin/python3

def uppercase(str):
    chars = ""
    for ch in str:
        if ord(ch) >= 97 and ord(ch) <= 122:
            ch = ord(ch) - 32
            ch = chr(ch)
        chars = chars + ch

    print("{}".format(chars))
