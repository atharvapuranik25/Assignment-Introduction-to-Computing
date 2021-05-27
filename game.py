"""
This module is a grid based game inspired from a game called Co Ganh
It is played on a 5x5 grid
It involves 2 players each with 8 pieces
First one to capture 7 of the other pieces wins
"""

import numpy as np
ROW = 5
COL = 5
turn = 0
points_1 = 0
points_2 = 0
board = np.zeros((ROW, COL))  # creating a grid of zeroes

def mark(row, col, player):  # marking positions on grid
    board[row][col] = player

def start():  # starting position
    mark(0, 0, 1)
    mark(1, 0, 1)
    mark(2, 0, 1)
    mark(3, 0, 1)
    mark(4, 0, 1)
    mark(0, 1, 1)
    mark(0, 2, 1)
    mark(4, 1, 1)
    mark(0, 3, 2)
    mark(0, 4, 2)
    mark(1, 4, 2)
    mark(2, 4, 2)
    mark(3, 4, 2)
    mark(4, 4, 2)
    mark(4, 3, 2)
    mark(4, 2, 2)
    print(board)

def move(row_p, col_p, row_n, col_n):
    """
    Takes row and column no. of the piece to be moved and the place it needs to be moved to
    Checks validity of the move
    Moves the piece
    """
    global turn, points_1, points_2
    if turn % 2 == 0:
        print("\nPlayer 1")
        row_p = int(input("Row no. of the piece you want to move (0-4): "))
        col_p = int(input("Column no. of the piece you want to move (0-4): "))
        row_n = int(input("Row no. of the block you want to move to (0-4): "))
        col_n = int(input("Column no. of the block you want to move to (0-4): "))
        if board[row_p][col_p] == 0 or board[row_p][col_p] == 2:
            print("Invalid move")
        else:
            if row_n > row_p + 1 or row_n < row_p - 1 or col_n > col_p + 1 or col_n < col_p - 1:
                print("Invalid move")
            else:
                if (row_p or row_n or col_p or col_n) > 4 or (row_p or row_n or col_p or col_n) < 0:
                    print("Invalid move")
                else:
                    mark(row_p, col_p, 0)
                    mark(row_n, col_n, 1)
                    capture_ganh_1(row_n, col_n)
                    capture_chet_1(row_n, col_n)
                    turn = turn + 1
                    print(board, "\n")
                    print("Points P-1: ", points_1)
                    print("Points P-2: ", points_2)
    else:
        print("\nPlayer 2")
        row_p = int(input("Row no. of the piece you want to move: "))
        col_p = int(input("Column no. of the piece you want to move: "))
        row_n = int(input("Row no. of the block you want to move to: "))
        col_n = int(input("Column no. of the block you want to move to: "))
        if board[row_p][col_p] == 0 or board[row_p][col_p] == 1:
            print("Invalid move")
        else:
            if row_n > row_p + 1 or row_n < row_p - 1 or col_n > col_p + 1 or col_n < col_p - 1:
                print("Invalid move")
            else:
                if (row_p or row_n or col_p or col_n) > 4 or (row_p or row_n or col_p or col_n) < 0:
                    print("Invalid move")
                else:
                    mark(row_p, col_p, 0)
                    mark(row_n, col_n, 2)
                    capture_ganh_2(row_n, col_n)
                    capture_chet_2(row_n, col_n)
                    turn = turn + 1
                    print(board, "\n")
                    print("Points P-1: ", points_1)
                    print("Points P-2: ", points_2)

def capture_ganh_1(row_n, col_n):
    """
    Takes the row and column no. of the piece
    Checks for captures
    Marks both the captured pieces 0
    """
    global points_1
    if col_n - 1 < 0 or col_n + 1 > 4:  # capturing at edges
        if board[row_n + 1][col_n] == 2 and board[row_n - 1][col_n] == 2:
            mark(row_n + 1, col_n, 0)
            mark(row_n - 1, col_n, 0)
            points_1 += 2
        else:
            pass
    elif row_n - 1 < 0 or row_n + 1 > 4:  # capturing at edges
        if board[row_n][col_n + 1] == 2 and board[row_n][col_n - 1] == 2:
            mark(row_n, col_n + 1, 0)
            mark(row_n, col_n - 1, 0)
            points_1 += 2
        else:
            pass
    else:  # capturing in the middle of the board
        if board[row_n + 1][col_n + 1] == 2 and board[row_n - 1][col_n - 1] == 2:
            mark(row_n + 1, col_n + 1, 0)
            mark(row_n - 1, col_n - 1, 0)
            points_1 += 2
        if board[row_n][col_n + 1] == 2 and board[row_n][col_n - 1] == 2:
            mark(row_n, col_n + 1, 0)
            mark(row_n, col_n - 1, 0)
            points_1 += 2
        if board[row_n + 1][col_n] == 2 and board[row_n - 1][col_n] == 2:
            mark(row_n + 1, col_n, 0)
            mark(row_n - 1, col_n, 0)
            points_1 += 2
        if board[row_n - 1][col_n + 1] == 2 and board[row_n + 1][col_n - 1] == 2:
            mark(row_n - 1, col_n + 1, 0)
            mark(row_n + 1, col_n - 1, 0)
            points_1 += 2

def capture_chet_1(row_n, col_n):
    """
    Takes row and column no. of the piece
    Checks for capture
    Marks the captured piece 0
    """
    global points_1
    try:
        if board[row_n + 2][col_n] == 1 and board[row_n + 1][col_n] == 2:
            mark(row_n + 1, col_n, 0)
            points_1 += 1
    except IndexError:
        pass
    try:
        if board[row_n + 2][col_n + 2] == 1 and board[row_n + 1][col_n + 1] == 2:
            mark(row_n + 1, col_n + 1, 0)
            points_1 += 1
    except IndexError:
        pass
    try:
        if board[row_n][col_n + 2] == 1 and board[row_n][col_n + 1] == 2:
            mark(row_n, col_n + 1, 0)
            points_1 += 1
    except IndexError:
        pass
    try:
        if board[row_n - 2][col_n + 2] == 1 and board[row_n - 1][col_n + 1] == 2:
            mark(row_n - 1, col_n + 1, 0)
            points_1 += 1
    except IndexError:
        pass
    try:
        if board[row_n - 2][col_n] == 1 and board[row_n - 1][col_n] == 2:
            mark(row_n - 1, col_n, 0)
            points_1 += 1
    except IndexError:
        pass
    try:
        if board[row_n - 2][col_n - 2] == 1 and board[row_n - 1][col_n - 1] == 2:
            mark(row_n - 1, col_n - 1, 0)
            points_1 += 1
    except IndexError:
        pass
    try:
        if board[row_n][col_n - 2] == 1 and board[row_n][col_n - 1] == 2:
            mark(row_n, col_n - 1, 0)
            points_1 += 1
    except IndexError:
        pass
    try:
        if board[row_n + 2][col_n - 2] == 1 and board[row_n + 1][col_n - 1] == 2:
            mark(row_n + 1, col_n - 1, 0)
            points_1 += 1
    except IndexError:
        pass

def capture_ganh_2(row_n, col_n):
    """
    Takes the row and column no. of the piece
    Checks for captures
    Marks both the captured pieces 0
    """
    global points_2
    if col_n - 1 < 0 or col_n + 1 > 4:  # capturing at edges
        if board[row_n + 1][col_n] == 1 and board[row_n - 1][col_n] == 1:
            mark(row_n + 1, col_n, 0)
            mark(row_n - 1, col_n, 0)
            points_2 += 2
        else:
            pass
    elif row_n - 1 < 0 or row_n + 1 > 4:  # capturing at edges
        if board[row_n][col_n + 1] == 1 and board[row_n][col_n - 1] == 1:
            mark(row_n, col_n + 1, 0)
            mark(row_n, col_n - 1, 0)
            points_2 += 2
        else:
            pass
    else:  # capturing in the middle of the board
        if board[row_n + 1][col_n + 1] == 1 and board[row_n - 1][col_n - 1] == 1:
            mark(row_n + 1, col_n + 1, 0)
            mark(row_n - 1, col_n - 1, 0)
            points_2 += 2
        if board[row_n][col_n + 1] == 1 and board[row_n][col_n - 1] == 1:
            mark(row_n, col_n + 1, 0)
            mark(row_n, col_n - 1, 0)
            points_2 += 2
        if board[row_n + 1][col_n] == 1 and board[row_n - 1][col_n] == 1:
            mark(row_n + 1, col_n, 0)
            mark(row_n - 1, col_n, 0)
            points_2 += 2
        if board[row_n - 1][col_n + 1] == 1 and board[row_n + 1][col_n - 1] == 1:
            mark(row_n - 1, col_n + 1, 0)
            mark(row_n + 1, col_n - 1, 0)
            points_2 += 2

def capture_chet_2(row_n, col_n):
    """
    Takes row and column no. of the piece
    Checks for capture
    Marks the captured piece 0
    """
    global points_2
    try:
        if board[row_n + 2][col_n] == 2 and board[row_n + 1][col_n] == 1:
            mark(row_n + 1, col_n, 0)
            points_2 += 1
    except IndexError:
        pass
    try:
        if board[row_n + 2][col_n + 2] == 2 and board[row_n + 1][col_n + 1] == 1:
            mark(row_n + 1, col_n + 1, 0)
            points_2 += 1
    except IndexError:
        pass
    try:
        if board[row_n][col_n + 2] == 2 and board[row_n][col_n + 1] == 1:
            mark(row_n, col_n + 1, 0)
            points_2 += 1
    except IndexError:
        pass
    try:
        if board[row_n - 2][col_n + 2] == 2 and board[row_n - 1][col_n + 1] == 1:
            mark(row_n - 1, col_n + 1, 0)
            points_2 += 1
    except IndexError:
        pass
    try:
        if board[row_n - 2][col_n] == 2 and board[row_n - 1][col_n] == 1:
            mark(row_n - 1, col_n, 0)
            points_2 += 1
    except IndexError:
        pass
    try:
        if board[row_n - 2][col_n - 2] == 2 and board[row_n - 1][col_n - 1] == 1:
            mark(row_n - 1, col_n - 1, 0)
            points_2 += 1
    except IndexError:
        pass
    try:
        if board[row_n][col_n - 2] == 2 and board[row_n][col_n - 1] == 1:
            mark(row_n, col_n - 1, 0)
            points_2 += 1
    except IndexError:
        pass
    try:
        if board[row_n + 2][col_n - 2] == 2 and board[row_n + 1][col_n - 1] == 1:
            mark(row_n + 1, col_n - 1, 0)
            points_2 += 1
    except IndexError:
        pass

def game_over():
    """
    Checks points of both players
    If equal to or more than 7
        Declares winner
        Game over
    Else returns False
    """
    if points_1 >= 7:
        print("Player 1 Wins!!!")
        print("Game Over")
    elif points_2 >= 7:
        print("Player 2 Wins!!!")
        print("Game Over")
    else:
        return False

def game(row_p, col_p, row_n, col_n):
    """
    Displays instructions and starts the game
    While game over condition is not reached, calls move
    """
    print("Assignment-1 - Grid Based Game\n")
    var = int(input("Enter 1 for instructions, 2 to start the game: "))
    if var == 1:
        print("\nInstructions\n")
        print("1. You can move your pieces to any adjacent empty space.")
        print("2. To capture an opponent's piece you have 2 options-")
        print("    a) place a piece between 2 of the opponent's pieces in a single line.")
        print("    b) cover the opponent's piece from 2 sides in a single line.")
        print("3. Each piece you capture gives you 1 point.")
        print("4. First one to capture 7 or more pieces wins.\n")
        start()
        while game_over() is False:
            move(row_p, col_p, row_n, col_n)
    elif var == 2:
        start()
        while game_over() is False:
            move(row_p, col_p, row_n, col_n)
    else:
        print("Enter a valid input. Try again.")

row1 = 0
col1 = 0
row2 = 0
col2 = 0
game(row1, col1, row2, col2)  # calls for the game to start
