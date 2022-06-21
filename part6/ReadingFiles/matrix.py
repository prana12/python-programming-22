def read_numbers():
    numbers = []

    with open("matrix.txt") as new_file:
        row = []
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(",")
            #print(parts)
            for i in parts:
                row.append(int(i))
            #print(row)
            numbers.append(row)
            row = []

    #print(numbers)
    return numbers

def matrix_sum():
    numbers = read_numbers()
    sum = 0

    for row in numbers:
        for number in row:
            sum += number
    
    return sum

def matrix_max():
    numbers = read_numbers()
    max_number = numbers[0][0] #0
    
    for row in numbers:
        for number in row:
            if number > max_number:
                max_number = number
        
    return max_number

def row_sums():
    numbers = read_numbers()
    sums = []

    for row in numbers:
        sum = 0
        for number in row:
            sum += number
        sums.append(sum)
    
    return sums

if __name__ == "__main__":
    sum = matrix_sum()
    print(sum)
    max = matrix_max()
    print(max)
    sums = row_sums()
    print(sums)