from Crypto.Cipher import AES
import hashlib

password = b'mypassword'
key = hashlib.sha256(password).digest()
mode = AES.MODE_CBC
IV = 'This is an IV456'


cipher = AES.new(key,mode,IV)

decrypted_text = cipher.decrypt(b"Y\xd6\x86\xf0'\xaeS\xbe\x00.\xbd\x97\xce\xec\x8c\x10\xb8\x0f\xd68P\xdd\xf4t\x13X\x16e\xa4\x0c\x17\xda")

print(decrypted_text.rstrip().decode())