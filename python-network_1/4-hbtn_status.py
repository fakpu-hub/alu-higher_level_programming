#!/usr/bin/python3
"""Fetches and displays the status from a local web server."""

import requests


def main():
    """Send a GET request and display the response body."""
    response = requests.get("http://0.0.0.0:5050/status")
    body = response.text

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))


if __name__ == "__main__":
    main()
