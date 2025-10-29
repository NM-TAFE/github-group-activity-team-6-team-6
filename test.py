import random

board = [' ', 'X', ' ',
         'O', 'X', 'O',
         ' ', ' ', 'O']
priority_moves = [4, 0, 2, 6, 8]
win_combinations = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
    (0, 4, 8), (2, 4, 6)  # Diagonal
]


def create_empty_cells_list():
    empty_cells = []
    # go through all cells in board to check if they are empty,
    # if so, add the index to the list
    for _ in range(len(board)):
        if board[_] == ' ':
            empty_cells.append(_)
    return empty_cells


# use symbol to allow the function to be used first to check for winning moves
# and then for blocking moves
def winning_move_search(symbol):
    empty_cells = create_empty_cells_list()
    # for every empty cell, check which winning combinations
    # is it a part of
    for empty_cell in empty_cells:
        for combination in win_combinations:
            # if the empty cell is in a combination, get the empty cell out of
            # it and add them to a list
            if empty_cell in combination:
                pairs = []
                for _ in range(len(combination)):
                    if combination[_] not in empty_cells:
                        pairs.append(combination[_])
                # if the "pairs" list is longer than 1 and the symbols on those indexes are matching,
                # return the empty cell index
                if len(pairs) > 1 and board[pairs[0]] == board[pairs[1]] == symbol:
                    return empty_cell
    return None


def check_winner(some_board):
    for combination in win_combinations:
        if some_board[combination[0]] == some_board[combination[1]] == some_board[combination[2]] != ' ':
            return some_board[combination[0]]
    return None


def fake_move(symbol):
    fake_board = board.copy()
    empty_cells = create_empty_cells_list()
    # for each empty cell, change the cell on the fake board
    # to the symbol passed as argument and check for win
    for empty_cell in empty_cells:
        fake_board[empty_cell] = symbol
        # if a win is detected, return the cell index
        if check_winner(fake_board) == symbol:
            return empty_cell
        # if no win, reset the cell to empty state
        else:
            fake_board[empty_cell] = ' '
    return None


def ai_move(player_symbol, ai_symbol):
    empty_cells = create_empty_cells_list()
    next_move = None
    if fake_move(ai_symbol) is not None:
        next_move = fake_move(ai_symbol)
    elif fake_move(player_symbol) is not None:
        next_move = fake_move(player_symbol)
    else:
        for empty_cell in empty_cells:
            if empty_cell in priority_moves:
                next_move = empty_cell
            else:
                next_move = random.choice(empty_cells)
    return next_move


print(f'Winning move search for O: {winning_move_search("O")}')
print(f'Winning move search for X: {winning_move_search("X")}')
print()
print(f'Fake move search for O: {fake_move("O")}')
print(f'Fake move search for X: {fake_move("X")}')
print()
print(f'Next move for ai: {ai_move("X", "O")}')

