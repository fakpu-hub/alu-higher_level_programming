#!/usr/bin/python3
"""This module defines Rectangle"""


class Rectangle(BaseGeometry):
    """Representation of a rectangle."""

    def __init__(self, width, height):
        """Initialize a rectangle with validated dimensions."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
