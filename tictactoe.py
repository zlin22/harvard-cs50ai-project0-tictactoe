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
    # return [[O, O, EMPTY],
    #         [X, X, EMPTY],
    #         [X, X, O]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_x = 0
    count_o = 0

    for row in board:
        for col in row:
            if col == X:
                count_x += 1
            elif col == O:
                count_o += 1
            else:
                pass

    if count_x > count_o:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    row_num = 0
    col_num = 0

    for row in board:
        for col in row:
            if col == EMPTY:
                actions.append((row_num, col_num))
            col_num += 1
        row_num += 1
        col_num = 0

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_dcopy = copy.deepcopy(board)
    row_num = 0
    col_num = 0

    current_player = player(board_dcopy)

    if action is None or board_dcopy[action[0]][action[1]] is not None:
        raise Exception("invalid move")

    for row in board_dcopy:
        for col in row:
            if row_num == action[0] and col_num == action[1]:
                board_dcopy[row_num][col_num] = current_player
            col_num += 1
        row_num += 1
        col_num = 0

    return board_dcopy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # check rows
    for row in board:
        values_in_row = set()
        for col in row:
            values_in_row.add(col)

        if values_in_row == {X}:
            return X
        elif values_in_row == {O}:
            return O
        else:
            pass

    # check cols
    for i_col in range(len(board)):
        values_in_col = set()
        for row in board:
            values_in_col.add(row[i_col])

        if values_in_col == {X}:
            return X
        elif values_in_col == {O}:
            return O
        else:
            pass

    # check diags
    values_in_diag1 = set()
    values_in_diag2 = set()
    for i_row in range(len(board)):
        for i_col in range(len(board)):
            if i_col == i_row:
                values_in_diag1.add(board[i_row][i_col])
            if i_col == len(board) - 1 - i_row:
                values_in_diag2.add(board[i_row][i_col])

    if values_in_diag1 == {X} or values_in_diag2 == {X}:
        return X
    elif values_in_diag1 == {O} or values_in_diag2 == {O}:
        return O
    else:
        pass

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
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    # X wants max value
    def max_value(board):
        if terminal(board):
            utility_board = utility(board)
            return utility_board
        v = -math.inf
        for action in actions(board):
            m = min_value(result(board, action))
            v = max(v, m)
        # print(v)
        return v

    # O wants min value
    def min_value(board):
        if terminal(board):
            utility_board = utility(board)
            return utility_board
        v = math.inf
        for action in actions(board):
            m = max_value(result(board, action))
            v = min(v, m)
        # print(v)
        return v

    optimal_action = None

    if player(board) == X:
        utility_list = []
        for action in actions(board):
            current_utility = min_value(result(board, action))
            utility_list.append(current_utility)
        optimal_utility = max(utility_list)
        index_optimal_utility = utility_list.index(optimal_utility)
        optimal_action = actions(board)[index_optimal_utility]

    else:
        utility_list = []
        for action in actions(board):
            current_utility = max_value(result(board, action))
            utility_list.append(current_utility)
        optimal_utility = min(utility_list)
        index_optimal_utility = utility_list.index(optimal_utility)
        optimal_action = actions(board)[index_optimal_utility]

    return optimal_action
