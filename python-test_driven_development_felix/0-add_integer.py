#!/usr/bin/python3
"""This module provides a function for adding two integers."""


def add_integer(a, b=98):
    """Add two numbers after converting floats to integers.

    Args:
        a: The first number.
        b: The second number, defaulting to 98.

    Returns:
        The integer sum of a and b.

    Raises:
        TypeError: If either argument is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
