numbers = []
item = 1

while True:
    print(f"The list is now {numbers}")
    option = input("a(d)d, (r)emove or e(x)it: ")
    if option.lower() == "x":
        print("Bye!")
        break
    elif option.lower() == "d":
        numbers.append(item)
        item += 1
    elif option.lower() == "r":
        numbers.pop(len(numbers)-1)
        item -= 1