my_list = []

while True:
    number = int(input("New item: "))
    if number == 0:
        print("Bye!")
        break
    my_list.append(number)
    print(f"The list now: {my_list}")
    print(f"The list in order: {sorted(my_list)}")