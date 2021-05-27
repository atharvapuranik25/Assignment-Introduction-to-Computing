import pygame, sys
import numpy as np

pygame.init()

ROWS, COLS = 5, 5
WIDTH, HEIGHT = 500, 500
CYAN = (0, 255, 255)
GRID_LINES = ("#007575")
P1_COLOR = ("#EAEB87")
P2_COLOR = ("#FF8E9C")
TURN = 0
points_1 = 0
points_2 = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ganh')
screen.fill(CYAN)

board = np.zeros((ROWS, COLS))  # creating a grid of zeroes

def grid(): # drawing grid on screen
    # horizontal lines
    pygame.draw.line(screen, GRID_LINES, (0, 100), (500, 100), 5)
    pygame.draw.line(screen, GRID_LINES, (0, 200), (500, 200), 5)
    pygame.draw.line(screen, GRID_LINES, (0, 300), (500, 300), 5)
    pygame.draw.line(screen, GRID_LINES, (0, 400), (500, 400), 5)

    # vertical lines
    pygame.draw.line(screen, GRID_LINES, (100, 0), (100, 500), 5)
    pygame.draw.line(screen, GRID_LINES, (200, 0), (200, 500), 5)
    pygame.draw.line(screen, GRID_LINES, (300, 0), (300, 500), 5)
    pygame.draw.line(screen, GRID_LINES, (400, 0), (400, 500), 5)

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


def draw_figures():
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, P1_COLOR, (int(col * 100 + 100 // 2), int(row * 100 + 100 // 2)), 20, 0)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, P2_COLOR, (int(col * 100 + 100 // 2), int(row * 100 + 100 // 2)), 20, 0)
            elif board[row][col] == 0:
                pygame.draw.circle(screen, CYAN, (int(col * 100 + 100 // 2), int(row * 100 + 100 // 2)), 20, 0)

def piece():
    global TURN
    if TURN % 2 == 0:
        if event.type == pygame.MOUSEBUTTONDOWN: #player1
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                row_p = int(pos[1] // 100)
                col_p = int(pos[0] // 100)
                if board[row_p][col_p] == 0 or board[row_p][col_p] == 2:
                    print("Invalid move")
                else:
                    mark(row_p, col_p, 0)
                    print(board)
                    draw_figures()
                    pygame.display.update()

            else:
                pos_n = pygame.mouse.get_pos()
                row_n = int(pos_n[1] // 100)
                col_n = int(pos_n[0] // 100)
                if board[row_n][col_n] == 2:
                    print("Invalid move")
                else:
                    mark(row_n, col_n, 1)
                    capture_ganh_1(row_n, col_n)
                    capture_chet_1(row_n, col_n)
                    print(board)
                    draw_figures()
                    pygame.display.update()
                    TURN += 1

    else:
        if event.type == pygame.MOUSEBUTTONDOWN: #player2
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                row_p = int(pos[1] // 100)
                col_p = int(pos[0] // 100)
                if board[row_p][col_p] == 0 or board[row_p][col_p] == 1:
                    print("Invalid move")
                else:
                    mark(row_p, col_p, 0)
                    print(board)
                    draw_figures()
                    pygame.display.update()

            else:
                pos_n = pygame.mouse.get_pos()
                row_n = int(pos_n[1] // 100)
                col_n = int(pos_n[0] // 100)
                if board[row_n][col_n] == 1:
                    print("Invalid move")
                else:
                    mark(row_n, col_n, 2)
                    capture_ganh_2(row_n, col_n)
                    capture_chet_2(row_n, col_n)
                    print(board)
                    draw_figures()
                    pygame.display.update()
                    TURN += 1


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



grid()
start()
draw_figures()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        piece()



    pygame.display.update()
