number = int(input("Please type in a number: "))
x = 1
while x <= number:
    y = 1
    while y <= number:
        print(f"{x} X {y} = {x*y} ") # , end=""
        y += 1
    x += 1