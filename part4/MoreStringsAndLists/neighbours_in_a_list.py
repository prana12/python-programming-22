def longest_series_of_neighbours(my_list:list):
    max = 0
    output = []

    for i in range(0, len(my_list)):
        count = 1
        output.append(my_list[i])
        
        while (i+count) < len(my_list):

            evaluate = (my_list[i+count-1]+1 ==  my_list[i+count]) or (my_list[i+count-1]-1 ==  my_list[i+count])
            if evaluate == True:
                output.append(my_list[i+count])
                count += 1
                if count > max:
                    max = count
            elif evaluate == False:
                output = []
                count = 1
                break

    return max

if __name__ == "__main__":
    #my_list = [1, 2, 5, 4, 3, 4]
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))