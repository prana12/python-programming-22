def same_chars(text, index1, index2):
    if index1 >= len(text) or index2 >= len(text):
        return False
    elif text[index1] == text[index2]:
        return True
    else:
        return False

if __name__ == "__main__":
    # same characters m and m
    print(same_chars("programmer", 6, 7)) # True

    # different characters p and r
    print(same_chars("programmer", 0, 4)) # False

    # the second index is not within the string
    print(same_chars("programmer", 0, 12)) # False