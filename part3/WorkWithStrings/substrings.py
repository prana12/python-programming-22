word = input("Please type in a string: ")

count = 0
# part1
while count < len(word):
    count += 1
    print(word[:(count)])
    
print("------------------")

# part2
count = 0
while count < len(word):
    count += 1
    print(word[len(word)-count:])