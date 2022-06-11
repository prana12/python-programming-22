word = input("Please type in a word: ")
character = input("Please type in a character: ")

#print(f"total length: {len(word)}, AND minus three = {len(word)-3}")

#count = 0
while True:
    if len(word) < 3:
        #print(f"ending WORD: {word}")
        break

    index = word.find(character)
    if index >= 0 and index+3 < len(word):
        print(f"{word[index:index+3]}")
        #print(index)
        word = word[index+1:]
        #print(f"matched WORD: {word}")
    else:
        word = word[1:]
        #print(f"not matched WORD: {word}")