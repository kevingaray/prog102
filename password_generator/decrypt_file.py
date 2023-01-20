from cryptography.fernet import Fernet
import random
import string

# opening the key
with open('password_generator/filekey.key', 'rb') as filekey:
	key = filekey.read()

# using the key
fernet = Fernet(key)
 
# opening the encrypted file
with open('password_generator/passwords_encrypted.txt', 'rb') as enc_file:
    encrypted = enc_file.read()
 
# decrypting the file
decrypted = fernet.decrypt(encrypted)
# opening the file in write mode and writing the decrypted data

# with open('password_generator/passwords_decrypted.txt', 'wb') as dec_file:
#     dec_file.write(decrypted)

def bytes_to_dic(decrypted):
    text = decrypted.decode('utf-8').split('\n')
    passwords = dict()
    for line in text:
        app,password=line.split(',')
        passwords[app]=password.strip()
    return passwords

def dic_to_bytes(passwords):
    text = ''
    for key,value in passwords.items():
        text += f"{key},{value}\n"
    return text.strip().encode('utf-8')


def generate_password(length=8):
    chars = string.ascii_letters + string.digits
    password = ''.join(random.choices(population=chars,k=length))
    return password

## main ##

# app_name = input("Enter app name: ")
# passwords = passwords_dic(decrypted)

# # verify if app is registered
# if app_name in passwords.keys():
#     print("App currently registered")
# # create new password
# else:
#     length = int(input("Insert length of password (min 8): "))
#     new_pass=generate_password(length)
#     print(f"Your password for {app_name} is : '{new_pass}'")
#     passwords[app_name]=new_pass

password = bytes_to_dic(decrypted)
print(password)
text = dic_to_bytes(password)

print(text)

    # ## encrypthing and save

encrypted = fernet.encrypt(text)

# # opening the file in write mode and writing the encrypted data
with open('password_generator/passwords_encrypted2.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)



