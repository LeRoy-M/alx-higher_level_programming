#!/usr/bin/python3
import dis
a = 98
def magic_calculation(a, b):
    a ** b
    a + b

dis.dis(magic_calculation)
