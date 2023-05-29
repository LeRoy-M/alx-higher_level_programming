#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    r = 0
    try:
        if (fct(*args)):
            r = (fct(*args))
            return (r)
    except Exception as err:
        print(f"Exception: {err}", file=sys.stderr)
        return (None)
