#!/usr/bin/python3
"""This module prints a square using the # character."""


def print_square(size):
    """Print a square of the specified size using # characters.

    Args:
        size: The length of each side of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is negative.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
