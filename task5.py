#!/usr/bin/python3

import hashlib

stored_hash = "482c811da5d5b4bc6d497ffa98491e38"
user_input = input("Enter password: ")

check_hash = hashlib.md5(user_input.encode()).hexdigest()

if check_hash == stored_hash:
    print("Password is correct")
else:
    print("Wrong password")

