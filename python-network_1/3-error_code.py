#!/usr/bin/python3
"""Fetches a URL and handles HTTP errors when requesting the resource."""

import urllib.request
import urllib.error
import sys


def main():
    """Fetch a URL and display its response body or HTTP error code."""
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))


if __name__ == "__main__":
    main()
