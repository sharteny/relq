#!/usr/bin/python3

failed_ips = {}

with open("/var/log/auth.log", "r") as file:
    for line in file:
        if "Failed password" in line:
            ip = line.split()[-1]

            if ip in failed_ips:
                failed_ips[ip] += 1
            else:
                failed_ips[ip] = 1

for ip, count in failed_ips.items():
    print(ip, "->", count)

