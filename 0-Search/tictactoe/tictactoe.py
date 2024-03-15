"""
Tic Tac Toe Player
"""

import copy
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
    number_of_x = sum(row.count(X) for row in board)
    number_of_o = sum(row.count(O) for row in board)
    return X if (number_of_x == number_of_o) else O 


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return [(i, j) for i, row in enumerate(board) for j, cell in enumerate(row) if cell == EMPTY]
    

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    i, j = action
    try:
        if board[i][j] != EMPTY:
            raise Exception("Invalid action: cell is not empty")
    except IndexError:
        raise Exception("Invalid action: index out of range")

    board_copy = copy.deepcopy(board)
    board_copy[i][j] = player(board)
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check rows
    for row in board:
        if row.count(X) == 3:
            return X
        elif row.count(O) == 3:
            return O
    
    # check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
        
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    has_winner = winner(board) is not None
    is_full = sum(row.count(EMPTY) for row in board) == 0

    return has_winner or is_full


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_is = winner(board)
    if winner_is == X:
        return 1
    elif winner_is == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    best_action = None
    alpha = -math.inf       # maximizer
    beta = math.inf         # minimizer

    if player(board) == X:
        best_val = -math.inf
        for action in actions(board):
            result_val = min_value(result(board, action), alpha, beta)
            if result_val > best_val:
                best_val = result_val
                best_action = action
            alpha = max(alpha, best_val)
    else:
        best_val = math.inf
        for action in actions(board):
            result_val = max_value(result(board, action), alpha, beta)
            if result_val < best_val:
                best_val = result_val
                best_action = action
            beta = min(beta, best_val)
    return best_action
    

def max_value(state, alpha, beta):
    if terminal(state):
        return utility(state)
    
    v = -math.inf
    for action in actions(state):
        v = max(v, min_value(result(state, action), alpha, beta))
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v


def min_value(state, alpha, beta):
    if terminal(state):
        return utility(state)
    
    v = math.inf
    for action in actions(state):
        v = min(v, max_value(result(state, action), alpha, beta))
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v
