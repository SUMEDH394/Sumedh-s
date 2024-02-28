import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Generate a password of default length (8 characters)
print("Generated Password:", generate_password())

# Generate a password of custom length
custom_length = int(input("Enter desired password length: "))
print("Generated Password:", generate_password(custom_length))

# generates the password of required length using "random"module.