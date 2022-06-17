def histogram(text: str):
    result = {}

    for letter in text:
        # if the letter is not yet in the dictionary, initialize the value to one
        if letter not in result:
            result[letter] = 1
        else:
            # increment the value
            result[letter] += 1
        
    #for key in result:
    #    print(f"{key} ", result[key]*"*")
    
    for key, value in result.items():
        print(f"{key} ", value*"*")

if __name__ == "__main__":
    histogram("abba")
    print()
    histogram("statistically")