import random
import string

def generate_password(length=12, include_special_chars=True, include_numbers=True):
    characters = string.ascii_letters

    if include_special_chars:
        characters += string.punctuation

    if include_numbers:
        characters += string.digits

    password = ''.join(random.choice(characters) for _ in range(length))
    return password
password = generate_password(length=16, include_special_chars=True, include_numbers=True)
print(password)
