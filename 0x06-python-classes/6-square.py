#!/usr/bin/python3
"""This module has the class `Square` that defines a square
with attribute `size`
"""


class Square:
    """This class defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """This method initializes the `Square` class
        Args:
            __size (int): measure of Square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """This method computes and returns the area of a square"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """This method computes and returns the area of a square"""
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) is not tuple or len(value) != 2 or
                type(value[0]) is not int or type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """This method computes and returns the area of a square"""
        return self.__size * self.__size

    def my_print(self):
        """This method prints in stdout the square with the character '#'"""
        if self.__size == 0:
            print()
            return
        else:
            for n in range(self.__position[1]):
                print()
            for y in range(self.__size):
                count = self.__position[0]
                if count > 0:
                    while count != 0:
                        print(end=" ")
                        count -= 1
                for x in range(self.__size):
                    print("{}".format("#"), end="")
                print()
            return
