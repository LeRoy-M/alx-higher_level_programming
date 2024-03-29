#!/usr/bin/python3
"""This module contains the 'is_same_class' function"""


def is_same_class(obj, a_class):
    """Function that returns 'True' if the object
    is exactly an instance of the specified class
    """
    if isinstance(obj, a_class) and type(obj) is a_class:
        return True
    return False
