#!/usr/bin/python3
"""This module contains a function that returns the list of available
    attributes and methods of an object
"""


def lookup(obj):
    """Function to retrun class object attributes list"""
    return list(dir(obj))
