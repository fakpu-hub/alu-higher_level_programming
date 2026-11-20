#!/usr/bin/python3
"""This module provides a function for converting objects to dictionaries."""


def class_to_json(obj):
    """Return the dictionary representation of an object's attributes."""
    return obj.__dict__
