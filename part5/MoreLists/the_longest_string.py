def longest(my_list:list):
    longest_string = []
    for word in my_list:
        if len(word) > len(longest_string):
            longest_string = word
    return longest_string

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))