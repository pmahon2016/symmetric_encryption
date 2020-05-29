from Crypto.Cipher import AES
import hashlib
import os

password = b'mypassword'
key = hashlib.sha256(password).digest()
mode = AES.MODE_CBC
IV = 'This is an IV456'

def pad_message(file):
    while len(file) % 16 != 0:
        file = file + b'0'
    return file


cipher = AES.new(key, mode, IV)

with open('my_secret_excel.xlsx','rb') as f:
    orig_file = f.read()





padded_file = pad_message(orig_file)


encrypted_message = cipher.encrypt(padded_file)

with open('encrypted_file', 'wb')as e:
    e.write(encrypted_message)

