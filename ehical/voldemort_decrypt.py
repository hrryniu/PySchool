#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet
#finding files

files=[] #creating list of files
for file in os.listdir(): #loop thats seeking for files
    if file == "voldemort.py" or file == "thekey.key" or file == "voldemort_decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files) #show all files in directiry

with open("thekey.key", "rb") as key: #read in binary mode -> "rb"
    secretkey = key.read()


#loop for every file in directory do decrypt
for file in files:
    with open(file, "rb") as thefile:
        content = thefile.read() #open file
    content_decrypted = Fernet(secretkey).decrypt(content) #encrypt
    with open(file, "wb") as thefile:
        thefile.write(content_decrypted) #write decrypted content into file

print(key)
