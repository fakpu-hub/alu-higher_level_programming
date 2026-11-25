#!/usr/bin/python3
"""Fetches and displays the status of the ALU intranet using requests."""

import requests


def main():
    """Send a GET request and display the response body."""
    response = requests.get("https://alu-intranet.hbtn.io/status")
    body = response.text

    print("Body response:")
    print("\t- {}".format(body))


if __name__ == "__main__":
    main()
