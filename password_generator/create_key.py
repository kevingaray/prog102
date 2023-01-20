# pip install cryptography
# import required module
from cryptography.fernet import Fernet

# key generation
key = Fernet.generate_key()
 
# string the key in a file
with open('password_generator/filekey.key', 'wb') as filekey:
   filekey.write(key)
