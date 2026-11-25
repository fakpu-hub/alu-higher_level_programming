#!/usr/bin/python3
"""Fetches a URL and displays the X-Request-Id response header."""

import requests
import sys


def main():
    """Send a GET request and display the X-Request-Id header."""
    response = requests.get(sys.argv[1])
    print(response.headers.get("X-Request-Id"))


if __name__ == "__main__":
    main()
