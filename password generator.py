import random
import string

app = input("Enter app name: ")
length = int(input("Enter length of password: "))

chars = string.ascii_letters + string.digits # + string.punctuation

def generate_password(length):
    password = ''
    for _ in range(length):
        password += random.choice(chars)
    return password

print(generate_password(length))