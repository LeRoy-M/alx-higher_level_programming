#!/usr/bin/python3
"""This module contains one function"""

def inherits_from(obj, a_class):
    """This function checks if an object is an instance of a 
    class that inherited from the specified class
    """
    return (isinstance(obj, a_class) and type(obj) != a_class)
