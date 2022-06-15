def no_vowels(text:str):
    vowel = ['a', 'e', 'i', 'o', 'u']
    text = text.lower()
    output = ""

    for i in text:
        if i not in vowel:
            output += i

    return output

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))