from Crypto.Cipher import AES
import hashlib
import os

password = b'mysecretpassword'
key = hashlib.sha256(password).digest()

cipher = AES.new(key, AES.MODE_CBC, 'This is an IV456')


decrypted_text = cipher.decrypt(b'L-\r\x95;\xec]z\xebx\x88\x9d\xc5\xcc\xe2\xf4j\xe3V\x97\x1b\t\xd2\x9c\xf7M\xaa\x93\xe4\xb9\x82b')
print(decrypted_text.rstrip().decode())

