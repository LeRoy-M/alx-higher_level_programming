#!/usr/bin/python3
"""This module contains a function that prints text with
2 new lines
"""


def text_indentation(text):
    """Function that prints text with 2 new lines
    after each '.', '?' and ':'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    x = 1
    for i, c in enumerate(text):
        if ord(c) == 32 and text[i - x] in [".", "?", ":"]:
            x += 1
            continue
        if c in [".", "?", ":"]:
            print(f"{c}\n")
            x = 1
            continue
        print(f"{c}", end="")
