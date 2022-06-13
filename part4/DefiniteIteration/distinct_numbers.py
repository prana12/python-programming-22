def distinct_numbers(my_list:list):
    distinct_list = []
    
    for i in my_list:
        if i not in distinct_list:
            distinct_list.append(i)

    return sorted(distinct_list)


if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]