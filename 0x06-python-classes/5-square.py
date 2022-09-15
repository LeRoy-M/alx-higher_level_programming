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
        self.size = size

    @property
    def size(self):
        """This method computes and returns the area of a square"""
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """This method computes and returns the area of a square"""
        return self.__size * self.__size

    def my_print(self):
        """This method prints in stdout the square with the character '#'"""
        if self.__size == 0:
            print()
            return
        else:
            area = self.__size * self.__size
            for y in range(self.__size):
                for x in range(self.__size):
                    print("{}".format('#'), end="")
                print()
            return
