#!/usr/bin/python3
"""This module provides a function for appending text to files."""


def append_write(filename="", text=""):
    """Append text to a UTF-8 file and return the number of
    characters added."""
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
