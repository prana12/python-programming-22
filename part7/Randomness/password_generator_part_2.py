from random import choice
import string

def generate_strong_password(length: int, digit_check: bool, special_check: bool):
    special_characters = "!?=+-()#."
    character = string.ascii_lowercase

    if digit_check:
        character += string.digits

    if special_check:
        character += special_characters


    while True:
        result = ""
        lowercase_included = False
        digit_included = False
        special_characters_included = False

        for i in range(length):
            selected = choice(character)
            
            if not lowercase_included and selected in string.ascii_lowercase:
                lowercase_included = True
            if not digit_included and digit_check:
                if selected in string.digits:
                    digit_included = True
            if not special_characters_included and special_check:
                if selected in special_characters:
                    special_characters_included = True

            result += selected

        if digit_check and special_check:
            if lowercase_included and digit_included and special_characters_included:
                break
        elif digit_check:
            if lowercase_included and digit_included:
                break
        elif special_check:
            if lowercase_included and special_characters_included:
                break
        else:
            if lowercase_included:
                break
    
    return result

if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(8, True, True))