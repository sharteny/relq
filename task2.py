#!/usr/bin/python3

import socket

domain = "localhost"
subs = ["www", "admin", "meet"]

for sub in subs:
    subdomain = sub + "." + domain
    try:
        ip = socket.gethostbyname(subdomain)
        print(f"[+] found {subdomain}->{ip}")
    except socket.gaierror:
        print(f"[-] not found {subdomain}")



