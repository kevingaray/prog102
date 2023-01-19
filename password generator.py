import random
import string

app = input("Enter app name: ")
length = int(input("Enter length of password: "))
punctuation = input("Do you want to consider punctuation characters (y/n): ")
punctuation_bool = True if punctuation in ['y','Y'] else False


def generate_password(length=8,punctuation_bool=False):
    chars = string.ascii_letters + string.digits
    if punctuation_bool: chars += string.punctuation
    password = ''.join(random.choices(population=chars,k=length))
    return password

print(f"Your password for {app} is: {generate_password(length,punctuation_bool)}")
