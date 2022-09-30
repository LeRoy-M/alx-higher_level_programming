#!/usr/bin/python3
"""This module creates a class 'Square'"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class is based on the previous module (9-rectangle.py)"""
    def __init__(self, size):
        """Initialization method that validates dimensions passed
        to it through inheritance of 'Rectangle' class

        Args:
            size (int): Value passed in
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """This method computes a square's area"""
        return self.__size ** 2
