from Crypto.Cipher import AES
import hashlib

password = b'mysecretpassword'
key = hashlib.sha256(password).digest()

cipher = AES.new(key, AES.MODE_CBC, 'This is an IV456')

orig_message = "this is the meaning of life"


def message_padding(message):
    while len(message) % 16 != 0:
        message = message + "0"
    return message

padded_message = message_padding(orig_message)

print(len(padded_message))

#
cipher_text = cipher.encrypt(padded_message)

print(cipher_text)

cipher1 = AES.new(key,AES.MODE_CBC,'This is an IV456')

decrypted_text = cipher1.decrypt(cipher_text)

print(decrypted_text.decode())
