#!/usr/bin/python3
"""This module contains the 'append_write' function"""


def append_write(filename="", text=""):
    """Function that appends a string at the end of a text file and
    returns the number of characters added
    """
    nc = 0
    for c in text:
        nc += 1

    with open(filename, mode="a", encoding="utf-8") as fn:
        fn.write(text)

    return nc
