print("Title: Password Encrypter\n")
print("Author: Justin Freese\n")
print("Date: 2/24/20\n\n")


import random
import string

i = input("Enter the password to be encrypted >>> \n".upper())

password = ''


for a in range(len(i)):
    new = random.choice(i + string.hexdigits)
    password += new

print('-------'*len(i))
print('New Password:', password)
print('-------'*len(i))
print("Old Password:", i)
print('-------'*len(i))

ask = input("Would you like to keep your old password? ")

if 'yes' in ask:
    print(i)
elif 'no' in ask:
    print("Ok, well here is your new password then --> ", password)
else:
    print("yes or no only...")