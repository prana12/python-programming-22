def most_common_character(text:str):
    if text == "":
        return "empty"
    text = sorted(text)
    max = 1
    maxCount = 1
    maxChar = text[0]
    output = []
    output.append(text[0])
    
    for i in range(1, len(text)):            
        if text[i] in output:
            max += 1
            if max > maxCount:
                maxCount = max
                maxChar = text[i]
        else:
            output.append(text[i])
            max = 1
    
    return maxChar

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))