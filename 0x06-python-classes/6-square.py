#!/usr/bin/python3
"""This module defines a class 'Square' based off of
the module '5-square'
"""


class Square:
    """The class 'Square' that has a private
    attribute
    """
    def __init__(self, size=0, position=(0, 0)):
        """The class is initialized here"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Getter method to retrieve 'size' field"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the value of an object variable 'size'"""
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """Getter method to retrieve the 'position' field"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Sets the value of an object's variable 'position'"""
        if (isinstance(value, tuple) and len(value) == 2):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Calculates the area of a square object and
        returns the value
        """
        return (self.__size * self.__size)

    def my_print(self):
        """Prints in stdout a square with the
        '#' character
        """
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            if (self.__position[0]):
                for k in range(self.__position[0]):
                    print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print("")
