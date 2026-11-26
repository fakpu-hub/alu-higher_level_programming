#!/usr/bin/python3
"""Fetches and displays the status from either server."""

import requests


def main():
    """Fetch a status response and display its type and content."""
    try:
        response = requests.get("http://0.0.0.0:5050/status")
        if response.status_code == 200:
            body = response.text
        else:
            response = requests.get("https://intranet.hbtn.io/status")
            body = response.text
    except requests.exceptions.RequestException:
        response = requests.get("https://intranet.hbtn.io/status")
        body = response.text

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))


if __name__ == "__main__":
    main()
