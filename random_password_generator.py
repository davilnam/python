import string
import random

LETTERS = string.ascii_letters # [a-zA-Z]
NUMBERS = string.digits # [0-9]
PUNCTUATION = string.punctuation 

def password_generator(length = 8):
    printable = f"{LETTERS}{NUMBERS}{PUNCTUATION}"
    printable = list(printable)
    random.shuffle(printable)
    random_password = random.choices(printable, k=length)
    random_password = "".join(random_password)
    return random_password

def get_password_length():
    password_length = int(input("How long do you want your password:"))
    return password_length

def main():
    password_length = get_password_length()
    password = password_generator(password_length)
    print(password)

if __name__ == "__main__":
    main()