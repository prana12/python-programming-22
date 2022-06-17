def count_matching_elements(m:list, num:int):
    matched = 0

    for i in range(len(m)): # using the number of rows in the matrix
        for j in range(len(m[i])): # using the number of items on each row 
            if m[i][j] == num:
                matched += 1
    return matched

if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))