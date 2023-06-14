#!/usr/bin/python3
"""This module contains the class 'MyList'"""


class MyList(list):
    """Defines the class 'MyList'"""
    def print_sorted(self):
        """Function that prints a list"""
        print(sorted(self))
