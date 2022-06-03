story = ""

while True:
    word = input("Please type in a word: ")
    if word == "end" or word in story.split():
        print(story)
        break
    story += word + " "