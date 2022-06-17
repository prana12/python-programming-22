def play_turn(game_board: list, x: int, y: int, piece: str):
    result = False

    # if the coordinates weren't valid
    if x >= 3 or y >= 3:
        return False

    #game_board[y][x] = 1
    item = game_board[y][x]
    print(item)

    if item == "":
        game_board[y][x] = piece
        result = True
    else:
        result = False
    
    return result

if __name__ == "__main__":
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 2, 0, "X"))
    print(game_board)