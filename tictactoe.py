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
    countX = 0
    countO = 0

    for row in board:
        for cell in row:
            if cell == X:
                countX += 1
            elif cell == O:
                countO += 1
    if countX == countO:
        return "X"
    else:
        return "O"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    action_options = set()

    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                action_options.add((i, j))
    
    return action_options


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    new_board = copy.deepcopy(board)
    if action not in actions(board):
        raise Exception("Action cannot be done, it's not possible")
    else:
        new_board[action[0]][action[1]] = player(board)
    return new_board
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    winning_check = [[(0,0), (0,1), (0,2)],
                     [(1,0), (1,1), (1,2)],
                     [(2,0), (2,1), (2,2)],
                     [(0,0), (1,0), (2,0)],
                     [(0,1), (1,1), (2,1)],
                     [(0,2), (1,2), (2,2)],
                     [(0,0), (1,1), (2,2)],
                     [(0,2), (1,1), (2,0)],]
    
    for check in winning_check:
        if board[check[0][0]][check[0][1]] == board[check[1][0]][check[1][1]] == board[check[2][0]][check[2][1]] != EMPTY:
            return board[check[0][0]][check[0][1]]
        
    return None
    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is not None:
        return True
    elif len(actions(board)) == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    else:
        # check if the game is over
        return 0


def max_value(board, is_root=True):
    if terminal(board) == True:
        return utility(board)
    
    possible_moves = actions(board)
    moves_score_dict = {}

    for move in possible_moves:
        # call the recursion function
        new_board = result(board, move)
        score = min_value(new_board, is_root=False)
        # choose whether minimax returns scores(int), tuple(move, score)
        if type(score) != int:    
            moves_score_dict[move] = score[1]
        else:
            moves_score_dict[move] = score
    
    # get the optimal moves
    optimal_action = max(moves_score_dict, key=moves_score_dict.get)
    
    # check if this is tree root
    if is_root == True:
        return optimal_action
    else:
        return (optimal_action, moves_score_dict[optimal_action])


def min_value(board, is_root=True):
    if terminal(board) == True:
        return utility(board)
    
    possible_moves = actions(board)
    moves_score_dict = {}

    for move in possible_moves:
        # call the recursion function
        new_board = result(board, move)
        score = max_value(new_board, is_root=False)
        # choose whether minimax returns scores(int), tuple(move, score)
        if type(score) != int:    
            moves_score_dict[move] = score[1]
        else:
            moves_score_dict[move] = score
    
    # get the optimal moves
    optimal_action = min(moves_score_dict, key=moves_score_dict.get)
    
    # check if this is tree root
    if is_root == True:
        return optimal_action
    else:
        return (optimal_action, moves_score_dict[optimal_action])



def minimax(board):
    if terminal(board) == True:
        return None
    
    if player(board) == "X":
        return max_value(board)

    else:
        return min_value(board)
    

# def minimax(board, is_root=True):
#     """
#     Returns the optimal action for the current player on the board.
#     """
#     # check if the game is over
#     if terminal(board) == True:
#         return utility(board)

#     # check for possible moves
#     possible_moves = actions(board)
#     moves_score_dict = {}
#     for move in possible_moves:
#         # call the recursion function
#         new_board = result(board, move)
#         score = minimax(new_board, is_root=False)
#         # choose whether minimax returns scores(int), tuple(move, score)
#         if type(score) != int:    
#             moves_score_dict[move] = score[1]
#         else:
#             moves_score_dict[move] = score

#     # given who's turn, and the score, try to get the optimal action
#     if player(board) == "X":
#         optimal_action = max(moves_score_dict, key=moves_score_dict.get)
#     else:
#         optimal_action = min(moves_score_dict, key=moves_score_dict.get)
    
#     # check if this is tree root
#     if is_root == True:
#         return optimal_action
#     else:
#         return (optimal_action, moves_score_dict[optimal_action])
    