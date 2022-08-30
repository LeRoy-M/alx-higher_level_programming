#!/usr/bin/python3

def element_at(my_list, idx):
    x = len(my_list) - 1
    if 0 > idx > x:
        return None
    else:
        return my_list[idx]
