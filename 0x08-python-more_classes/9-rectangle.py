#!/usr/bin/python3
"""This module has the class `Rectangle` that defines a rectangle
with attributes `width` and `height`
"""


class Rectangle:
    """This class defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """This method initializes the `Rectangle` class
        Args:
            width (int): measure of Rectangle
            height (int): measure of Rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """This method computes and returns the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """This method computes and returns the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """This method returns the area with the character '#'"""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            rec = ""
            for y in range(self.__height - 1):
                rec += (str(str(self.print_symbol) * self.width) + "\n")
            rec += str(str(self.print_symbol) * self.width)
            return rec

    def __repr__(self):
        """This method returns the area in an unambiguous manner"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """This method returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """This method returns a new `Rectangle` instance with
        width == height == size
        """
        return cls(size, size)

    def __del__(self):
        """This method prints a message to stdout when an instance
        is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
