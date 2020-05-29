from Crypto.Cipher import AES
import hashlib

password = b'mypassword'
key = hashlib.sha256(password).digest()
mode = AES.MODE_CBC
IV = 'This is an IV456'

cipher = AES.new(key,mode,IV)

with open('Encrypted_file','rb' ) as e:
    encrypted_file = e.read()

decrypted_file = cipher.decrypt(encrypted_file)

with open('decrypted_excel.xlsx', 'wb') as df:
    df.write(decrypted_file.rstrip(b'0'))

