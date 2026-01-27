#!/usr/bin/python3
import socket

target_ip = input("Enter IP address to scan:")

print(f"Scanning {target_ip} started...")

for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    result = s.connect_ex((target_ip, port))

    if result == 0:
        print(f"port {port} open")
    else:
        print(f"port {port} closed")

    s.close()

print("end.")
