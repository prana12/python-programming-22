from math import sqrt

while True:
    number = int(input("Please type in a number, 0 to quit: "))
    if number == 0:
        break
    elif number < 0:
        print("Invalid number")
    else:
        print(sqrt(number))