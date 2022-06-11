number = int(input("Please type in a number: "))

count = 1
while count <= number:
    if count+1 <= number:
        print(count+1)
    print(count)
    count += 2