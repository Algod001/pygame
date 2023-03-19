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
    prev = board[0][0]
    prev2 = board[0][0]
    for i in range(3):
        j=0
        if board[i][j]==board[i][j+1]==board[i][j+2]:
            return board[i][j]
        if board[j][i]==board[j+1][i]==board[j+2][i]:
            return board[j][i]
    if board[0][0]== board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2]== board[1][1] == board[2][0]:
        return board[0][2]


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board)== X or (winner(board)== O):
        return True
    elif actions(board) == None:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) ==O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
