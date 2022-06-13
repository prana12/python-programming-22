def list_sum(my_list1:list, my_list2:list):
    res_list = []
    
    for i in range(0, len(my_list1)):
        res_list.append(my_list1[i]+my_list2[i])

    return res_list


if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]