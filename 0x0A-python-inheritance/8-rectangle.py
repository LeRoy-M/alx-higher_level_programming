#!/usr/bin/python3
"""This module creates a class 'Rectangle'"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class is based on the previous module (7-base_geometry.py)"""
    def __init__(self, width, height):
        """Initialization method that validates dimensions passed
        to it through inheritance of 'BaseGeometry' class

        Args:
            width (int): Value passed for validation
            height (int): Value passed for validation
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
