#!/usr/bin/python3
class LockedClass:
    __slots__ = ["first_name"]
    """
    def __init__(self):
        first_name = setattr(self, self.__dict__["first_name"], self.first_name)
    def __setattr__(self, name, value):
        if name == "first_name":
            #self.__dict__[name] = value
    """
