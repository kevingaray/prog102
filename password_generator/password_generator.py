from cryptography.fernet import Fernet
import random
import string

# Procces : decryp text -> dictionary -> append password -> encryp dictionary

def bytes_to_dic(decrypted: bytes) -> dict:
    text = decrypted.decode('utf-8').split('\n')
    passwords = dict()
    for line in text:
        app,password=line.split(',')
        passwords[app]=password.strip()
    return passwords

def dic_to_bytes(passwords: dict) -> bytes:
    text = ''
    for key,value in passwords.items():
        text += f"{key},{value}\n"
    return text.strip().encode('utf-8')

def print_passwords(passwords: dict):
    print("All passwords")
    for app,password in passwords.items():
        print(f"{app}: '{password}'")

def generate_password(length=8) -> str:
    chars = string.ascii_letters + string.digits
    password = ''.join(random.choices(population=chars,k=length))
    return password

# opening the key
with open('password_generator/filekey.key', 'rb') as filekey:
	key = filekey.read()  # 44jd0HOyE7YbFGUeqL6I-HNoTrmcQSDUJ6mNZtgzCcw=

# using the key
fernet = Fernet(key)
 
# opening the encrypted file
with open('password_generator/passwords_encrypted.txt', 'rb') as enc_file:
    encrypted = enc_file.read()
 
# decrypting the file
decrypted = fernet.decrypt(encrypted)

# saving decrypting file in dictionary
passwords = bytes_to_dic(decrypted)

## main ##
option = int(input("Welcome to password generator, select option: \n(1) See all paswords\n(2) Insert new password\n"))
if option==1:
    print_passwords(passwords)
elif  option==2:
    app_name = input("Enter app name: ")
    # verify if app is registered
    if app_name in passwords.keys():
        print("App currently registered")
    # create new password
    else:
        length = int(input("Insert length of password (min 8): "))
        new_pass=generate_password(length)
        print(f"Your password for {app_name} is : '{new_pass}'")
        # save new password in dictonary
        passwords[app_name]=new_pass
        # encrypting passwords
        text = dic_to_bytes(passwords)
        encrypted = fernet.encrypt(text)
        # opening the file in write mode and saving the encrypted data
        with open('password_generator/passwords_encrypted.txt', 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
else:
    print('Invalid options')
