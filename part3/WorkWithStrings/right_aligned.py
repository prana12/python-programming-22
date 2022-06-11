word = input("Please type in a string: ")
count = 0
pos = 20-len(word)

output = ""

while count < 20:
    if count < pos:
        output += "*"
    else:
        output += word[count-pos]
    count += 1

print(output)