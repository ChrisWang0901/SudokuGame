import random


def check_column(board, x, y, value):
    return not value in board[x]


def check_row(board, x, y, value):
    for i in range(9):
        if board[i][y] == value:
            return False
    return True


def check_box(board, x, y, value):
    box_start_x = x // 3 * 3
    box_start_y = y // 3 * 3
    for x in range(box_start_x, box_start_x + 3):
        for y in range(box_start_y, box_start_y + 3):
            if board[x][y] == value:
                return False

    return True


def valid(board, x, y, value):
    """
    Check if the value is valid to put in (x,y) cell
    in the board
    """
    return check_box(board, x, y, value) and check_column(board, x, y, value) and check_row(board, x, y, value)

