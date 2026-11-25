#!/usr/bin/python3
"""Sends a letter to a search API and displays the JSON response."""

import requests
import sys


def main():
    """Send a POST request and process the returned JSON data."""
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    response = requests.post(
        "http://0.0.0.0:5000/search_user",
        data={"q": q}
    )

    try:
        data = response.json()
    except ValueError:
        print("Not a valid JSON")
        return

    if not data:
        print("No result")
    else:
        print("[{}] {}".format(data.get("id"), data.get("name")))


if __name__ == "__main__":
    main()
