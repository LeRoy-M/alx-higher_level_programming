#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = dict(a_dictionary)
    for k in new_dict.keys():
        new_dict[k] = new_dict[k] * 2

    return (new_dict)