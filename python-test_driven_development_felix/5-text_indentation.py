#!/usr/bin/python3
"""This module prints text with indentation after specific characters."""


def text_indentation(text):
    """Print text with two newlines after ., ? and : characters.

    Args:
        text: The string to format and print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    skip_space = False

    for char in text:
        if skip_space and char == " ":
            continue

        result += char
        skip_space = False

        if char in ".?:":
            result += "\n\n"
            skip_space = True

    print(result.strip(), end="")
