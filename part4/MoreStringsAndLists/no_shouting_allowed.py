def no_shouting(my_list:list):
    output = []

    for i in my_list:
        if not i.isupper():
            output.append(i)

    return output

if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)