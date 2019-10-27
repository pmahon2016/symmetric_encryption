from cryptography.fernet import Fernet

fkey = open("file_key.txt",'rb')
key = fkey.read()
cipher = Fernet(key)

filename = 'secret_excel.xltx'

with open(filename,'rb')as f:
    e_file = f.read()

encrypted_file = cipher.encrypt(e_file)

with open(filename + "encrypted",'wb') as ef:
    ef.write(encrypted_file)



