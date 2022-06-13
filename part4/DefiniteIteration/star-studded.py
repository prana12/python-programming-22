def star_studded():
    text = input("Please type in a string: ")

    for character in text:
        print(character + "\n*")

if __name__ == "__main__":
    star_studded()