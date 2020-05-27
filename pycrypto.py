from Crypto.Cipher import AES
import hashlib
import os

password = b'mysecretpassword'
key = hashlib.sha256(password).digest()

cipher = AES.new(key, AES.MODE_CBC, 'This is an IV456')

orig_message = "this is the meaning of life"


def message_padding(message):
    while len(message) % 16 != 0:
        message = message + b'0'
    return message


with open('secret_excel.xltx','rb') as ptxt:
    plaintext = ptxt.read()
    os.remove('secret_excel.xltx')

pad_plaintext = message_padding(plaintext)

cipher_text = cipher.encrypt(pad_plaintext)

with open ('Encrypted_file', 'wb') as efile:
    efile.write(cipher_text)

cipher1 = AES.new(key,AES.MODE_CBC,'This is an IV456')
#
decrypted_text = cipher1.decrypt(cipher_text)

dfile = open('decrypted file.xltx', 'wb')
dfile.write(decrypted_text.rstrip(b'0'))
