num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
choice = str(input("Operation: "))


if choice == "add":
    print(f"{num1} + {num2} = {num1 + num2}")
if choice == "multiply":
    print(f"{num1} * {num2} = {num1 * num2}")
if choice == "subtract":
    print(f"{num1} - {num2} = {num1 - num2}")