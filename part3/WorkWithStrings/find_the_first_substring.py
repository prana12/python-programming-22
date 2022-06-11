word = input("Please type in a word: ")
character = input("Please type in a character: ")

index = word.find(character)
if index >= 0:
    print(f"{word[index:index+3]}")