#!/usr/bin/python3
"""
Write a Python script that takes in a URL,
sends a request to the URL and displays the body of the response.
"""
import requests
import sys


def main():
    url = sys.argv[1]

    res = requests.get(url)
    if res.status_code >= 400:
        print("Error code: ", res.status_code)
    else:
        print(res.text)


if __name__ == "__main__":
    main()