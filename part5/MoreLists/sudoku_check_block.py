def block_correct(sudoku: list, row_no: int, column_no: int):
    validate_block = True
    valid_board_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    tracked_block_numbers = []

    for row in range(row_no, row_no+3):
        for col in range(0,3):
            item = sudoku[row][column_no + col]
            if item in tracked_block_numbers and item in valid_board_numbers:
                validate_block = False
            elif item == 0:
                continue
            else:
                tracked_block_numbers.append(item)
    
    return validate_block

if __name__ == "__main__":
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(block_correct(sudoku, 0, 0))
    print(block_correct(sudoku, 1, 2))