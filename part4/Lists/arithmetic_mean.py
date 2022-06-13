def mean(my_list: list):
    sum = 0
    count = 0

    while count < len(my_list):
        sum += my_list[count]
        count += 1

    return sum/len(my_list)

my_list = [1, 2, 3, 4, 5]
result = mean(my_list)
print("mean value is", result)