from random import choice
import string

def generate_password(length: int):
    result = ""

    for i in range(length):
        result += choice(string.ascii_lowercase)

    return result

if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))