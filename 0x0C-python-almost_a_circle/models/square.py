#!/usr/bin/python3
"""This module contains the 'Square' class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class 'Square' declared and defined"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization method"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String method to represent class instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.x}\
/{self.y} - {self.width}"

    @property
    def size(self):
        """Getter method that retrieves 'size' attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Getter method that retrieves 'size' attribute"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Method for updating field attributes"""
        if 'id' in kwargs and len(args) == 0:
            self.id = kwargs['id']
        elif len(args) > 0:
            self.id = args[0]
        if 'size' in kwargs and len(args) < 2:
            self.width = kwargs['size']
            self.height = kwargs['size']
        elif len(args) > 1:
            self.width = args[1]
            self.height = args[1]
        if 'x' in kwargs and len(args) < 3:
            self.x = kwargs['x']
        elif len(args) > 2:
            self.x = args[2]
        if 'y' in kwargs and len(args) < 4:
            self.y = kwargs['y']
        elif len(args) > 3:
            self.y = args[3]

    def to_dictionary(self):
        """Method that returns dictionary representation of
        a 'Square' instance
        """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
