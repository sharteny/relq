#!/usr/bin/python3

import requests

base_url = "http://127.0.0.1"

words = ["admin", "login", "test", "backup"]

for word in words:
    url = base_url + word
    try:
        r = requests.get(url, timeout=5)
        if r.status_code in [200, 301, 302, 403]:
            print(f"[+] {url}-> {r.status_code}")
    except requests.exceptions.RequestException:
        print(f"[-]  Error connecting to  {url}")
