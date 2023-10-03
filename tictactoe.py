"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def create_board(a,b,c,d,e,f,g,h,i):
    return [[a, b, c],
            [d, e, f],
            [g, h, i]]

def board_values(board):
    """
    This function returns the same board with the values
    X = 1
    O = -1
    """
    d = {"X": 1, "O": -1, None: 0}
    for ix, i in enumerate(board):
        for jx, j in enumerate(i):
            board[ix][jx] = d[j]
    return board


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    sum_of_board = 0
    for line in board:
        for i in line:
            if i:
                sum_of_board += 1

    #sum of board is odd -> turn of O
    #sum of board is even -> turn of X
    #sum of board is 9 -> return "Game Over"

    if sum_of_board == 9:
        return "Game Over"

    remainder = sum_of_board % 2
    return "X" if remainder == 0 else "O"



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for ix,i in enumerate(board):
        for jx,j in enumerate(i):
            if j == EMPTY:
                actions.add((ix, jx))

    return actions




def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY:
        raise Exception("Invalid action")
    else:
        p = player(board)
        board[action[0]][action[1]] = p
        return board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winner = None

    #check horizontal
    for line in range(3):
        if board[line][0] == board[line][1] == board[line][2]:
            winner = board[line][0]
            return winner

    #check vertical
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            winner = board[0][col]
            return winner

    #check diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        winner = board[0][0]
        return winner
    elif board[0][2] == board[1][1] == board[2][0]:
        winner = board[0][2]
        return winner

    return winner


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError


if __name__ == "__main__":

    initial = create_board(EMPTY,X, O, X, O, EMPTY, O, EMPTY, EMPTY)
    w = winner(initial)

    print(w)