from cryptography.fernet import Fernet

key = input("Please input your key: ")

cipher = Fernet(key)

filename = 'secret_excel.xltx'

with open(filename,'rb')as f:
    e_file = f.read()

encrypted_file = cipher.encrypt(e_file)

with open("encrypted_" + filename,'wb') as ef:
    ef.write(encrypted_file)



