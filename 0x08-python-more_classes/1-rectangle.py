#!/usr/bin/python3
"""This module has the class `Rectangle` that defines a rectangle
with attributes `width` and `height`
"""


class Rectangle:
    """This class defines a rectangle"""
    def __init__(self, width=0, height=0):
        """This method initializes the `Rectangle` class
        Args:
            width (int): measure of Rectangle
            height (int): measure of Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """This method accesses the field attribute `width`"""
        return self.__width

    @width.setter
    def width(self, width):
        """This method mutates the field attribute `width`"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        """This method accesses the field attribute `height`"""
        return self.__height

    @height.setter
    def height(self, height):
        """This method mutates the field attribute `height`"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
