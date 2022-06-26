import string

def separate_characters(my_string: str):
    first = ""
    second = ""
    third = ""

    for letter in my_string:
        #print(letter)
        if letter in string.ascii_letters:
            first += letter
        elif letter in string.punctuation:
            second += letter
        else:
            third += letter

    return (first, second, third)

if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])