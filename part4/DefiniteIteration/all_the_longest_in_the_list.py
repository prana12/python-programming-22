def all_the_longest(my_list:list):
    output = []
    output.append(my_list[0])
    longest = len(output[0])

    for i in range(1, len(my_list)):
        if len(my_list[i]) == longest:
            output.append((my_list[i]))
        elif len(my_list[i]) > longest:
             longest = len(my_list[i])
             output = []
             output.append(my_list[i])

    return output


if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = all_the_longest(my_list)
    print(result)

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result)