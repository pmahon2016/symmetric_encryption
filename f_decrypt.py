from cryptography.fernet import Fernet

fkey = input("Enter your key:")
# key = fkey.read()
cipher = Fernet(fkey)

with open('secret_excel.xltxencrypted','rb') as df:
    encrypted_data = df.read()


decrypted_file = cipher.decrypt(encrypted_data)

with open('secret_excel decrypted.xltx','wb') as df:
    df.write(decrypted_file)