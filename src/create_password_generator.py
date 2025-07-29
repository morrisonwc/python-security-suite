# create_password_generator.py
import random

def create_password_generator(characters):
    def create_password(length):
        output = []
        for i in range(length):
            output.append(random.choice(characters))
        return ''.join(output)
    return createPassword

def create_password_checker(min_uppercase, min_lowercase, min_punctuation, min_digits):
    def check_password(password):
        

my_new_password = createPasswordGenerator("abcdefgh1234567890_")

print(my_new_password(10))

