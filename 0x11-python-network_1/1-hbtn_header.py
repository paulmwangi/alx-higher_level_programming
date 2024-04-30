#!/usr/bin/python3
"""
Displays the value of the X-Request-Id variable
found in the header of the response
"""
import urllib.request
from sys import argv

def main():
    if len(argv) != 2:
        print("Usage: {} <URL>".format(argv[0]))
        sys.exit(1)

    url = argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            headers = response.info()
            print(headers['X-Request-Id'])
    except urllib.error.URLError as e:
        print("Error fetching URL:", e)

if __name__ == "__main__":
    main()
