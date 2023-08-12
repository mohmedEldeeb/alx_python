#!/usr/bin/python3
"""
import request package
"""
import requests


def main():

    req = requests.get('https://alu-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type:", (type(req.text)))
    print("\t- content:", req.text)


if __name__ == "__main__":
    main()