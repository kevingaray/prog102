# # run 'pip install pycryptodome'
import random
import string

def generate_password(length=8):
    chars = string.ascii_letters + string.digits
    password = ''.join(random.choices(population=chars,k=length))
    return password

def dictionary_passwords(file):
    next(file)
    passwords = dict()
    for line in file:
        app,password=line.split(',')
        passwords[app]=password.strip()
    return passwords

with open("passwords.csv",'r+') as file:
    passwords = dictionary_passwords(file)
    app_name = input("Enter app name: ")
    
    # verify if app is registered
    if app_name in passwords.keys():
        print("App currently registered")
    # create new password
    else:
        length = int(input("Insert length of password (min 8): "))
        new_pass=generate_password(length)
        print(f"Your password for {app_name} is : '{new_pass}'")
        # save it in file
        file.write(f"\n{app_name},{new_pass}")
        file.close()


