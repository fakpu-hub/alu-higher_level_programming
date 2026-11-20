#!/usr/bin/python3
"""This module provides a function for saving objects as JSON files."""

import json


def save_to_json_file(my_obj, filename):
    """Write an object's JSON representation to a text file."""
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)
