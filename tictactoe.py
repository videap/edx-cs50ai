"""
Tic Tac Toe Player
"""

import math
import copy

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
        return None

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
        new_board = copy.deepcopy(board)
        new_board[action[0]][action[1]] = p
        return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winner = None

    #check horizontal
    for line in range(3):
        if board[line][0] == board[line][1] == board[line][2] != None:
            winner = board[line][0]
            return winner

    #check vertical
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != None:
            winner = board[0][col]
            return winner

    #check diagonals
    if board[0][0] == board[1][1] == board[2][2] != None:
        winner = board[0][0]
        return winner
    elif board[0][2] == board[1][1] == board[2][0] != None:
        winner = board[0][2]
        return winner

    return winner


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return bool(winner(board) or not player(board))

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    d = {"X": 1, "O": -1, None: 0}
    w = winner(board)
    return d[w]

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # player X wants to maximize, player O wants to minimize
    p = player(board)
    if p == X:
        return max_value(board)[1]
    elif p == O:
        return min_value(board)[1]

def max_value(board):
    if terminal(board):
        return (utility(board), None)
    else:
        moves = actions(board)
        value = -100
        for m in moves:
            next_board = result(board, m)
            mx = max(value, min_value(next_board)[0])
            if mx > value:
                value = mx
                best_move = m
        return (value, best_move)

def min_value(board):
    if terminal(board):
        return (utility(board), None)
    else:
        moves = actions(board)
        value = 100
        for m in moves:
            next_board = result(board, m)
            mn = min(value, max_value(next_board)[0])
            if mn < value:
                value = mn
                best_move = m
        return (value, best_move)