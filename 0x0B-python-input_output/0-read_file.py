#!/usr/bin/python3
"""This module contains the 'read_file' function"""


def read_file(filename=""):
    """Function that reads a text file and
    prints it to stdout
    """
    with open(filename, mode="r", encoding="UTF-8") as fn:
        print(fn.read(), end="")
