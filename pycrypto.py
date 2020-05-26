"""this is for PyCrypto"""
from Crypto.Cipher import AES
from Crypto import Random

key = Random.new()
print(key.read(16))
print(key)

cipher = AES.new("mywordismybond88",AES.MODE_CBC,'This is an IV456')

message = "super secret msg"

cipher_text = cipher.encrypt(message)

print(cipher_text)

cipher1 = AES.new("mywordismybond88",AES.MODE_CBC,'This is an IV456')

decrypted_text = cipher1.decrypt(cipher_text)

print(decrypted_text.decode())