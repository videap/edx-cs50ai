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
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


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

    initial = create_board(X,O,X,X,O,X,O,X,O)
    print(initial)
    a = actions(initial)
    print(a)