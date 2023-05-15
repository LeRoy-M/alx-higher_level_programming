#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    new_tpl = []
    if len(tuple_a) == len(tuple_b) == 2:
        new_tpl = [(tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1])]
    elif len(tuple_a) == 2 and len(tuple_b) == 1:
        new_tpl = [(tuple_a[0] + tuple_b[0]), (tuple_a[1] + 0)]
    elif len(tuple_a) == 1 and len(tuple_b) == 2:
        new_tpl = [(tuple_a[0] + tuple_b[0]), (0 + tuple_b[1])]
    elif len(tuple_a) == 2 and len(tuple_b) == 0:
        new_tpl = [(tuple_a[0] + 0), (tuple_a[1] + 0)]
    elif len(tuple_a) == 0 and len(tuple_b) == 2:
        new_tpl = [(0 + tuple_b[0]), (0 + tuple_b[1])]
    elif len(tuple_a) == len(tuple_b) == 1:
        new_tpl = [(tuple_a[0] + tuple_b[0]), (0 + 0)]
    elif len(tuple_a) == 1 and len(tuple_b) == 0:
        new_tpl = [(tuple_a[0] + 0), (0 + 0)]
    elif len(tuple_a) == 0 and len(tuple_b) == 1:
        new_tpl = [(0 + 0), (tuple_b[0] + 0)]
    elif len(tuple_a) == len(tuple_b) == 0:
        new_tpl = [0, 0]
    return (tuple(new_tpl))
