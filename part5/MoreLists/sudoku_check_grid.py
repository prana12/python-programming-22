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

def sudoku_grid_correct(sudoku: list):
    validate_grid = True

    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            #print(f"({row},{col})")
            #print(sudoku[row][col])
            if block_correct(sudoku, row, col) == False:
                validate_grid = False

    return validate_grid

if __name__ == "__main__":
    sudoku1 = [
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

print(sudoku_grid_correct(sudoku1))

sudoku2 = [
  [2, 6, 7, 8, 3, 9, 5, 0, 4],
  [9, 0, 3, 5, 1, 0, 6, 0, 0],
  [0, 5, 1, 6, 0, 0, 8, 3, 9],
  [5, 1, 9, 0, 4, 6, 3, 2, 8],
  [8, 0, 2, 1, 0, 5, 7, 0, 6],
  [6, 7, 4, 3, 2, 0, 0, 0, 5],
  [0, 0, 0, 4, 5, 7, 2, 6, 3],
  [3, 2, 0, 0, 8, 0, 0, 5, 7],
  [7, 4, 5, 0, 0, 3, 9, 0, 1]
]

print(sudoku_grid_correct(sudoku2))