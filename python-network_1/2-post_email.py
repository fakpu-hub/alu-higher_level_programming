#!/usr/bin/python3
"""Sends an email parameter through a POST request and displays the response."""

import urllib.request
import urllib.parse
import sys


def main():
    """Sends an email using POST and displays the response."""
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({"email": email}).encode("utf-8")
    request = urllib.request.Request(url, data=data)

    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))


if __name__ == "__main__":
    main()
