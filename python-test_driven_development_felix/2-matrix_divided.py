#!/usr/bin/python3
"""This module divides all elements of a matrix by a given number."""


def matrix_divided(matrix, div):
    """Divide every element in a matrix and round to two decimal places.

    Args:
        matrix: A list of lists containing integers or floats.
        div: The number to divide each element by.

    Returns:
        A new matrix containing the divided values.

    Raises:
        TypeError: If the matrix, its rows, or div has an invalid type.
        ZeroDivisionError: If div is zero.
    """
    if (not isinstance(matrix, list) or not matrix or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_size = len(matrix[0])

    for row in matrix:
        if len(row) != row_size:
            raise TypeError(
                "Each row of the matrix must have the same size"
            )

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) "
                    "of integers/floats"
                )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row]
            for row in matrix]
