#!/usr/bin/python3
"""This module provides a function for loading objects from JSON files."""

import json


def load_from_json_file(filename):
    """Create and return a Python object from a JSON file."""
    with open(filename, mode="r", encoding="utf-8") as file:
        return json.load(file)
