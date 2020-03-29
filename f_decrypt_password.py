from cryptography.fernet import Fernet

key = input("Enter your key:")

cipher = Fernet(key)

with open('encrypted_secret_excel.xltx', 'rb') as df:
    encrypted_data = df.read()


decrypted_file = cipher.decrypt(encrypted_data)

with open('decrypted_secret_excel.xltx','wb') as df:
    df.write(decrypted_file)