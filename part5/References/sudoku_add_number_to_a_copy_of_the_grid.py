def print_sudoku(sudoku: list):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            item = sudoku[i][j]
            if item == 0:
                print("- ", end="")
            else:
                print(f"{item} ", end="")
        print()

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int) -> list:
    # working example:
    my_list_copy = []
    
    for i in range(len(sudoku)):
        my_list_copy.append([])
        for j in range(len(sudoku[i])):
            #my_list_copy[i][j] = sudoku[i][j]
            my_list_copy[i].append(sudoku[i][j])
    
    my_list_copy[row_no][column_no] = number
    return my_list_copy
    
    """ my_list_copy = sudoku[:]
    print(id(sudoku[row_no][column_no]))
    print(id(my_list_copy[row_no][column_no]))
    my_list_copy[row_no][column_no] = number

    print(sudoku)
    print(my_list_copy)
    return my_list_copy """


if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)