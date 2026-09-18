import random
import string

def generate_password(length=12):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    all_chars = lowercase + uppercase + digits
    password_chars = random.choices(all_chars, k=length)
    random.shuffle(password_chars)
    password = ''.join(password_chars)
    return password

password = generate_password(10)
print("Generated Password:", password)
