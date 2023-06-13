#!/usr/bin/python3
"""This module contains the 'write_file' function"""


def write_file(filename="", text=""):
    """Function that writes a string to a text file (UTF-8), and
    returns the number of characters written to it
    """
    nc = 0
    for c in text:
        nc += 1

    with open(filename, mode="w", encoding="utf-8") as fn:
        fn.write(text)

    return nc
