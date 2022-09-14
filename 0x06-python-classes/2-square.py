#!/usr/bin/python3
"""This module has the class `Square` that defines a square
with attribute `size`
"""


class Square:
    """This class defines a square"""
    def __init__(self, size=0):
        """This method initializes the `Square` class
        Args:
            __size (int): measure of Square
        """
        self.__size = size
