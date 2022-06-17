def add_item(my_list: list) -> list:
    new_item = 10
    my_list_copy = my_list[:]
    #my_list_copy.append(new_item)
    my_list_copy[0] = new_item

    print(id(my_list[0]))
    print(id(my_list_copy[0]))

    return my_list_copy

if __name__ == "__main__":
    numbers = [1, 2, 3]
    numbers2 = add_item(numbers)

    print("original list:", numbers)
    print("new list:", numbers2)