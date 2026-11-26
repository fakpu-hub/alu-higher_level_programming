#!/usr/bin/python3
"""This module prints a person's full name."""


def say_my_name(first_name, last_name=""):
    """Print a person's first name and last name.

    Args:
        first_name: The person's first name.
        last_name: The person's last name, defaulting to an empty string.

    Raises:
        TypeError: If either name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
