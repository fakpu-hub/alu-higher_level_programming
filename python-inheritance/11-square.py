#!/usr/bin/python3
"""Defines a Square class."""
class Square(Rectangle):
    """Representation of a square."""

    def __init__(self, size):
        """Initialize a square with a validated size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the square's area."""
        return self.__size ** 2

    def __str__(self):
        """Return the square description."""
        return "[Square] {}/{}".format(
            self.__size, self.__size
        )
