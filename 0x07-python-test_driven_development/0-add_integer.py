#!/usr/bin/python3
"""Takes two integers as input and adds them together.
    Args:
        a (int/ float): First Input
        b (int/ float): Second Input
"""


def add_integer(a, b=98):
    """Adds two integers.
        Returns a + b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a + b)
