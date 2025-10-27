from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialise game board and current player
board = [' '] * 9
current_player = 'X'


def check_winner():
    # Winning combinations
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
        (0, 4, 8), (2, 4, 6)  # Diagonal
    ]
    for combination in win_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] != ' ':
            return board[combination[0]]
    return None


def check_draw():
    return ' ' not in board



@app.route('/')
def index():
    winner = check_winner()
    draw = check_draw()
    return render_template('index.html',
                           board=board,
                           current_player=current_player,
                           winner=winner,
                            draw=draw)

# LINEAR SEARCH
# def ai_move(symbol):
#     win_conditions = [
#         (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
#         (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
#         (0, 4, 8), (2, 4, 6)  # Diagonal
#     ]
#     # initialize a position int which will be used to get an index
#     # on the board in case there is a winning move to be made
#     position = -1
#     # go through the winning conditions and compare in pairs,
#     # if there are 2 symbols in a condition and an empty spot, the empty spot
#     # will be the position to take for the next move
#     for condition in win_conditions:
#         if board[condition[0]] == board[condition[1]] != ' ' and board[condition[2]] == ' ':
#             position = condition[2]
#         elif board[condition[0]] == board[condition[2]] != ' ' and board[condition[1]] == ' ':
#             position = condition[1]
#         elif board[condition[1]] == board[condition[2]] != ' ' and board[condition[0]] == ' ':
#             position = condition[0]
#     if position != -1:
#         board[position] = symbol


# @app.route('/play_ai/<int:cell>')
# def play_ai(cell):
#     global current_player
#     if board[cell] == ' ':
#         board[cell] = current_player
#         if not check_winner():
#             ai_move('O')
#     return redirect(url_for('index'))

@app.route('/play/<int:cell>')
def play(cell):
    # breakpoint()
    global current_player
    if board[cell] == ' ':
        board[cell] = current_player
        if not check_winner():
            current_player = 'O' if current_player == 'X' else 'X'
    return redirect(url_for('index'))


@app.route('/reset')
def reset():
    global board, current_player
    board = [' '] * 9
    current_player = 'X'
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
