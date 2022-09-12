#!/usr/bin/python3

def raise_exception_msg(message=""):
    try:
        print(f"{message}")
    except NameError:
        print(f"{message}")
