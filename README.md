URLChecker
==========

URLChecker is a simple Python script that reads URLs from standard input, checks their availability using HTTP HEAD requests, and saves the URLs that are reachable (status code 200) to an output file.

Features
--------
- Read URLs from standard input.
- Check the availability of each URL using HTTP HEAD requests.
- Save reachable URLs to an output file.
- Print the location of the saved file.

Prerequisites
-------------
- Python 3.x
- `requests` library

You can install the required library using pip:

    pip install requests

Usage
-----
1. Run the script using Python and provide the URLs via standard input:

    python main.py

2. The script will save the reachable URLs to `urls.txt`.

Example
-------
    $ python main.py
    http://example.com
    http://nonexistent.com
    http://example.org

    Saved URLs to: urls.txt
