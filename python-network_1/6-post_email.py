#!/usr/bin/python3
"""Sends an email through a POST request and displays the response body."""

import requests
import sys


def main():
    """Send an email parameter using POST and display the response."""
    url = sys.argv[1]
    email = sys.argv[2]

    response = requests.post(url, data={"email": email})
    print(response.text)


if __name__ == "__main__":
    main()
