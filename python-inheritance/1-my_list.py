#!/usr/bin/python3
"""t"""


class MyList(list):
    """A custom list class."""

    def print_sorted(self):
        """Print the list in ascending order."""
        print(sorted(self))
