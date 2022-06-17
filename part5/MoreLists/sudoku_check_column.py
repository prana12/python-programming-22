def column_correct(game_board: list, col_no: int):
    validate_col = True
    valid_board_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    tracked_col_numbers = []

    for row in game_board:
        item = row[col_no]
        if item in tracked_col_numbers and item in valid_board_numbers:
            validate_col = False
        elif item == 0:
            continue
        else:
            tracked_col_numbers.append(item)
    
    return validate_col


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

    print(column_correct(sudoku, 0))
    print(column_correct(sudoku, 1))