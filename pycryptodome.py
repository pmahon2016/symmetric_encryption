from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

key = b'mysecretpassword'

cipher = AES.new(key, AES.MODE_CBC)
data = b"this is my super secret message"

cipher_text = cipher.encrypt(pad(data, AES.block_size))

with open('pycryptodome_key', 'wb') as kfile:
    kfile.write(cipher.iv)
    kfile.write(cipher_text)







