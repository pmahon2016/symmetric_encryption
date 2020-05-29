from Crypto.Cipher import AES
import hashlib
import os

password = b'mysecretpassword'
key = hashlib.sha256(password).digest()

cipher = AES.new(key, AES.MODE_CBC, 'This is an IV456')


decrypted_text = cipher.decrypt(b'(n\xed\x8e\x05\x030!U\x07\xfeQ\xf4 @\x8fI\x11\x1f\x96n\x98JF\x9d\xe0\x1a\x1ce\xce\x1fY'
)
print(decrypted_text.rstrip().decode())

