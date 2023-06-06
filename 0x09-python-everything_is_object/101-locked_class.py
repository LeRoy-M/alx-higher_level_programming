#!/usr/bin/python3
class LockedClass:
    #first_name = setattr(self, name, value)
    def __setattr__(self, name, value):
        if name == "first_name":
            self.__dict__[name] = value
