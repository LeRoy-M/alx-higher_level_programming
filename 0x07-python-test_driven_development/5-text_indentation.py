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
    for c in text:
        if c in [".", "?", ":"]:
            print(f"{c}\n")
            continue
        print(f"{c}", end="")
