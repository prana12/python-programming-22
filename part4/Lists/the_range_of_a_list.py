def range_of_list(my_list:list):
    my_list.sort()
    return my_list[len(my_list)-1] - my_list[0]

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    result = range_of_list(my_list)
    print("The range of the list is", result)