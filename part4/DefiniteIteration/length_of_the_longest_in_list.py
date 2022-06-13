def length_of_longest(my_list:list):
    longest = 0

    """ for i in my_list:
        if len(i) > longest:
            longest = len(i) """

    for i in range(1, len(my_list)):
        if len(my_list[i]) > longest:
            longest = len(my_list[i])

    return longest


if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = length_of_longest(my_list)
    print(result)