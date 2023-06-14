#!/usr/bin/python3
"""This module contains the 'is_kind_of_class' function"""


def is_kind_of_class(obj, a_class):
    """Function that returns 'True' if the object is an
    instance of the specified class, or if the object
    is an instance of a class that inherited from
    said class
    """
    if isinstance(obj, a_class):
        return True
    return False
