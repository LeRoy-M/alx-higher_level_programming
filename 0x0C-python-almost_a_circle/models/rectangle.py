#!/usr/bin/python3
"""This module contains the 'Rectangle' class"""
from models.base import Base


class Rectangle(Base):
    """Class 'Rectangle' declared and defined"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization method"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter method retrieves 'width' attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method that sets value for 'width' attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter method that retrieves 'height' attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method that sets value for 'height' attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter method that retrieves 'x' attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method that sets value for 'x' attribute"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter method that retrieves 'y' attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method that sets value for 'y' attribute"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def __str__(self):
        """String method to represent class instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.x}\
/{self.y} - {self.width}/{self.height}"

    def area(self):
        """Method that computes area of a rectangle"""
        return self.width * self.height

    def display(self):
        """Method that prints to stdout the 'Rectangle' instance
        with the character '#'
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x, end='')
            print("#" * self.width)

    def update(self, *args, **kwargs):
        """Method to assign an argument to each attribute"""
        if 'id' in kwargs and len(args) == 0:
            self.id = kwargs['id']
        elif len(args) > 0:
            self.id = args[0]
        if 'width' in kwargs and len(args) < 2:
            self.width = kwargs['width']
        elif len(args) > 1:
            self.width = args[1]
        if 'height' in kwargs and len(args) < 3:
            self.height = kwargs['height']
        elif len(args) > 2:
            self.height = args[2]
        if 'x' in kwargs and len(args) < 4:
            self.x = kwargs['x']
        elif len(args) > 3:
            self.x = args[3]
        if 'y' in kwargs and len(args) < 5:
            self.y = kwargs['y']
        elif len(args) > 4:
            self.y = args[4]

    def to_dictionary(self):
        """Method that returns dictionary representation of
        a 'Rectangle' instance
        """
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
