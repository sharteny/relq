#!/usr/bin/python3

import paramiko

host = "127.0.0.1"
username = input("Username: ")
password = input("Password: ")

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    client.connect(
        host,
        username=username,
        password=password,
        timeout=5
    )
    print("[+] SSH connection successful!")

    stdin, stdout, stderr = client.exec_command("whoami")
    print("Command output:", stdout.read().decode())

    client.close()

except paramiko.AuthenticationException:
    print("[-] Authentication failed")

except paramiko.SSHException as e:
    print("[-] SSH error:", e)

except Exception as e:
    print("[-] Error:", e)

