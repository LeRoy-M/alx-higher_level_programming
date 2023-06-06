#!/usr/bin/python3
"""This module defines the class 'Rectangle' based on module '5-rectangle'"""


class Rectangle:
    """Defines a class 'Rectangle'"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Intializes 'Rectangle' instance with optional width and
        height fields set to '0'
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Method to print the rectangle with the character '#'"""
        shape = ""
        if (self.__width == 0 or self.__height == 0):
            return (shape)
        for j in range(self.__height - 1):
            shape += ((str("#") * self.__width) + "\n")
        shape += (str("#") * self.__width)
        return (shape)

    def __repr__(self):
        """Method to return a string representation of the rectangle"""
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        """Method to delete an instance of the 'Rectangle' class"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Function to retrieve private instance attribute 'width'"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Function to set private instance attribute 'width'"""
        if not (isinstance(value, int)):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Function to retrieve private instance attribute 'height'"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Function to set private instance attribute 'height'"""
        if not (isinstance(value, int)):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Function that calculates and returns the area of a rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Function that calculates and returns the perimeter of a rectangle"""
        if (self.__width == 0 or self.__height == 0):
            return (0)
        return ((self.__width + self.__height) * 2)
