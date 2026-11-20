#!/usr/bin/python3
"""This module defines a Rectangle class based on BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle with validated private dimensions."""

    def __init__(self, width, height):
        """Initialize a rectangle with a validated width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle description."""
        return "[Rectangle] {}/{}".format(
            self.__width, self.__height
        )
