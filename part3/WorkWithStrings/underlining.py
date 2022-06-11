word = input("Please type in a string: ")
count = len(word)
output = ""

while count > 0:
    output += "-"
    count -= 1

print (word)
print (output)