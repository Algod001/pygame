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


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j]:
                count+=1
    if count%2 ==0:
        return X
    elif count%2==1:
        return O
    elif count==O:
        return initial_state()


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    act = []
    for i in range(3):
        for j in range(3):
            if board[i][j]:
                act.append(board[i][j])
                
    return set(act)

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    move = board.copy()
    move[i][j] = player(board)                     #############################
    return move

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    countx=0
    county=0
    countnone=0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                countx+=1
            elif board[i][j] == O:
                county+=1
            else:
                countnone+=1


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
