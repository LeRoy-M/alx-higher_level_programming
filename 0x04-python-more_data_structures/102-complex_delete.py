#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    to_del = []
    for i in a_dictionary.items():
        if i[1] == value:
            to_del.append(i[0])
    for k in to_del:
        del a_dictionary[k]
    return (a_dictionary)
