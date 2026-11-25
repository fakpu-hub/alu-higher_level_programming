#!/usr/bin/python3
"""Fetches a URL and displays the X-Request-Id response header."""

import urllib.request
import sys


def main():
    """Send a request and display the X-Request-Id response header."""
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers.get("X-Request-Id"))


if __name__ == "__main__":
    main()
