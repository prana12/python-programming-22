def first_word(sentence):
    endIndex = sentence.find(" ")
    return sentence[0:endIndex]

def second_word(sentence):
    firstIndex = sentence.find(" ") 
    sub_sentence = sentence[firstIndex+1:]
    endIndex = sub_sentence.find(" ")
    return sub_sentence[0:endIndex]

def last_word(sentence):
   last_word = ""
   while True:
        index = sentence.find(" ")
        if index >= 0:
            sentence = sentence[index+1:]
            last_word = sentence
        else:
            break

   return last_word

if __name__ == "__main__":
    sentence = "it was a dark and stormy python"

    print(first_word(sentence)) # it
    print(second_word(sentence)) # was
    print(last_word(sentence)) # python