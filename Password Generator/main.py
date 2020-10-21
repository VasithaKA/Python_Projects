import string
import random


def passwordGenerator(length=4):
    source = string.digits + string.ascii_letters + string.punctuation
    password = random.choice(string.digits) + random.choice(string.ascii_lowercase) + \
        random.choice(string.ascii_uppercase) + \
        random.choice(string.punctuation)
    for _ in range(length-4):
        password += random.choice(source)
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    return password


length = int(input("Enter the password length (minimum length is 4): "))
print("Your Password is \"" + passwordGenerator(length) + "\"")
