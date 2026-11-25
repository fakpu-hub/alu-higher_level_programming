#!/usr/bin/python3
"""Displays the GitHub user ID using Basic Authentication."""

import requests
import sys


def main():
    """Authenticate with GitHub and display the user's ID."""
    username = sys.argv[1]
    password = sys.argv[2]

    response = requests.get(
        "https://api.github.com/user",
        auth=(username, password)
    )

    print(response.json().get("id"))


if __name__ == "__main__":
    main()
