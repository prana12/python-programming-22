word = input("Please type in a string: ")
character = input("Please type in a substring: ")
character_length = len(character)

times = 0
count = 0
result = ""

while count < len(word)-character_length:
    if word[count:count+character_length] == character:
        times += 1
        if times == 2:
            result = str(count)
            break
    count += 1

if result == "":
    print("The substring does not occur twice in the string.")
else:
    print(f"The second occurrence of the substring is at index {result}.")