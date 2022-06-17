def row_correct(game_board: list, row_no: int):
    validate_row = True
    valid_board_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    tracked_row_numbers = []

    row = game_board[row_no]
    for item in row:
        if item in tracked_row_numbers and item in valid_board_numbers:
            validate_row = False
        elif item == 0:
            continue
        else:
            tracked_row_numbers.append(item)
    
    return validate_row


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

    print(row_correct(sudoku, 0))
    print(row_correct(sudoku, 1))