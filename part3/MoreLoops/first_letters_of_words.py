sentence = input("Please type in a sentence: ")

count = 0

while count < len(sentence):
    if count == 0 or sentence[count-1] == " ":
        print(sentence[count])
    count += 1