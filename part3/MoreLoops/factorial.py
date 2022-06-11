input = input("Please type in a number: ")
number = int(input)
res = 1;

if number <= 0:
    print("Thanks and bye!")
else:
    while number > 1:
        res *= number
        number -= 1
    print(f"The factorial of the number {input} is {res}")