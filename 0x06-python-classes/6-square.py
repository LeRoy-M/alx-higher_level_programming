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
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def position(self):
        """This method computes and returns the area of a square"""
        return self.__position

    @position.setter
    def position(self,position):
        if type(position) is not tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """This method computes and returns the area of a square"""
        return self.__size * self.__size

    def my_print(self):
        """This method prints in stdout the square with the character '#'"""
        if self.__size == 0:
            print()
            return
        else:
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
