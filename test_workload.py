#!/usr/bin/env python3
"""
Run this script for creating n requests to a web service
"""

import requests
import sys
import time

URL = "83.160.85.219"

if __name__ == '__main__':

    if len(sys.argv) != 3:
        print("Usage: {} url n".format(sys.argv[0]))

    _, url, n = sys.argv

    for i in range(int(n)):
        r = requests.get(url=url)
        print("{}. status: {}".format(i, r.status_code))
        time.sleep(0.01)  # sleep 10 ms
