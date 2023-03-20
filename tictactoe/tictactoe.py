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
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                count += 1
    if count % 2 == 0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    act = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                act.add((i, j))
    return act


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid Action!!!")

    b2 = copy.deepcopy(board)
    b2[action[0]][action[1]] = player(board)
    
    return b2

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        j=0
        if board[i][j]==board[i][j+1]==board[i][j+2]!= EMPTY:
            return board[i][j] 
        if board[j][i]==board[j+1][i]==board[j+2][i]!= EMPTY:
            return board[j][i]
    if board[0][0]== board[1][1] == board[2][2]!= EMPTY:
        return board[0][0]
    if board[0][2]== board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board)== X or (winner(board)== O):
        return True
    elif not actions(board):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w == X:
        return 1
    elif w == O:
        return -1
    else:
        return 0
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if player(board) == X:
        return max_value(board)[1]
    elif player(board) == O:
        return min_value(board)[1]
    
def max_value(board):
    """
    Returns the maximum possible value for the current player on the board.
    """
    vma = float('-inf')
    move = None
    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        vma = max(vma, min_value(result(board, action)[0]))
        if vma > (min_value(result(board, action)[0])
    return [vma, move]

def min_value(board):
    """
    Returns the minimum possible value for the current player on the board.
    """
    vmi = float('inf')
    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        vmi = min(vmi, max_value(result(board, action)[0]))
        if vma > ( max_value(result(board, action)[0]):
    return [vmi, move]


