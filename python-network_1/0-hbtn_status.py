#!/usr/bin/python3
"""Fetches and displays the status from either server."""

import urllib.request
import urllib.error


def main():
    """Fetch the status and display its bytes and decoded content."""
    url = "http://0.0.0.0:5050/status"

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
    except urllib.error.URLError:
        url = "https://alu-intranet.hbtn.io/status"
        with urllib.request.urlopen(url) as response:
            body = response.read()

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode("utf-8")))


if __name__ == "__main__":
    main()
