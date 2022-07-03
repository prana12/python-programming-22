import string

def change_case(orig_string: str):
    result = ""

    for letter in orig_string:
        if letter.islower():
            result += letter.upper()
        elif letter.isupper():
            result += letter.lower()
        else:
            result += letter
    
    return result

def split_in_half(orig_string: str):
    mid = len(orig_string)//2
    
    return (orig_string[:mid], orig_string[mid:])

def remove_special_characters(orig_string: str):
    result = ""

    for letter in orig_string:
        if letter not in string.punctuation:
            result += letter

    return result

if __name__ == "__main__":
    print()
    #print(change_case("Well hello there!"))
    #print(split_in_half("Well hello there!"))
    #print(remove_special_characters("This is a test, lets see how it goes!!!11!"))