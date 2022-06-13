my_list = [1, 2, 3, 4, 5]
print(my_list)

while True:
    index = int(input("Index: "))
    if index == -1:
        break
    value = int(input("New value: "))

    my_list[index] = value
    print(my_list)