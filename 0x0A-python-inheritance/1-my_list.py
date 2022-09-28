#!/usr/bin/python3
"""This module creates a class that inherits from 'list'

    Args:
        list (int): Class parameter
"""


class MyList(list):
    """This class inherits from list"""
    def ___init__(self):
        """Initialization method"""
        super().__init__()

    def print_sorted(self):
        """This method prints a sorted list"""
        print (sorted(self))
