#!/usr/bin/python3
"""Fetches and displays the response body from the ALU intranet."""

import urllib.request


def main():
    """Fetch the ALU intranet status and display its response body."""
    with urllib.request.urlopen("https://alu-intranet.hbtn.io/status") as response:
        body = response.read()
        print("Body response:")
        print("\t- {}".format(body))


if __name__ == "__main__":
    main()
