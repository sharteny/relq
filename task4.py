#!/usr/bin/python3

hash = input("Enter hash:").strip()

length = len(hash) 

if(length == 30):
    print("Possible hash type: MD5")
elif(length == 40):
    print("Possible hash type: SHA1")
elif(length == 56):
    print("Possible hash type: SHA224")
elif length == 64:
    print("Possible hash type: SHA256")
elif length == 96:
    print("Possible hash type: SHA384")
elif length == 128:
    print("Possible hash type: SHA512")
else:
    print("Unknown hash type")
