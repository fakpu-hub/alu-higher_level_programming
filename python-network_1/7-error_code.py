#!/usr/bin/python3
"""Fetches a URL and handles HTTP error status codes."""

import requests
import sys


def main():
    """Fetch a URL and display its body or HTTP error code."""
    response = requests.get(sys.argv[1])

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)


if __name__ == "__main__":
    main()
