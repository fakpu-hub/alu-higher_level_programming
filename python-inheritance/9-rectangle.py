#!/usr/bin/python3
"""Defines a Rectangle class."""

class Rectangle(BaseGeometry):
    """Representation of a rectangle."""

    def __init__(self, width, height):
        """Initialize a rectangle with validated dimensions."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Return the rectangle's area."""
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle description."""
        return "[Rectangle] {}/{}".format(
            self.__width, self.__height
        )
