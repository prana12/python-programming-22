def who_won(game_board: list):
    player1_score = 0
    player2_score = 0

    for i in range(len(board)): # using the number of rows in the matrix
        for j in range(len(board[i])): # using the number of items on each row 
            if board[i][j] == 1:
                player1_score += 1
            elif board[i][j] == 2:
                player2_score += 1
    if player1_score > player2_score:
        return 1
    elif player2_score > player1_score:
        return 2
    else:
        return 0


if __name__ == "__main__":
    board = [[1, 2, 1], [2, 2, 2], [1, 0, 0]]
    print(who_won(board))