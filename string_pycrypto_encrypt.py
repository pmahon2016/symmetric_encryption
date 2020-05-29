from Crypto.Cipher import AES
import hashlib
import os

def message_padding(message):
    while len(message) % 16 != 0:
        message = message + ' '
    return message

password = b'mysecretpassword'
key = hashlib.sha256(password).digest()

cipher = AES.new(key, AES.MODE_CBC, 'This is an IV456')

orig_message = "this is the meaning of life"

padded_message = message_padding(orig_message)

print(len(padded_message))

encrypted_text = cipher.encrypt(padded_message)
print(encrypted_text)
