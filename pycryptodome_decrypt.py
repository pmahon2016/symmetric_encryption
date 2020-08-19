from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

key = b'mysecretpassword'

with open('pycryptodome_key','rb') as c_text:
    iv = c_text.read(16)
    ct = c_text.read()

cipher = AES.new(key, AES.MODE_CBC, iv)
pt = unpad(cipher.decrypt(ct), AES.block_size)

print(pt.decode())