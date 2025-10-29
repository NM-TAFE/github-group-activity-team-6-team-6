from flask import Flask, render_template, request, redirect, url_for
import ai_bot

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
def choice():
    return render_template('choice.html')
#
#
# @app.route('/two_players')
# def two_players():
#     winner = check_winner()
#     draw = check_draw()
#     return render_template('index.html',
#                            board=board,
#                            current_player=current_player,
#                            winner=winner,
#                            draw=draw)
#
# @app.route('/ai_play')
# def ai_play():
#     ai_bot.ai_move("X", "O")
#     winner = check_winner()
#     draw = check_draw()
#

@app.route('/play')
def index():
    winner = check_winner()
    draw = check_draw()
    if current_player == 'O' and len(ai_bot.create_empty_cells_list(board))>0:
        cell = ai_bot.ai_move(board, "X", "O")
        play(cell)
    return render_template('index.html',
                           board=board,
                           current_player=current_player,
                           winner=winner,
                            draw=draw)


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
    app.run(debug=True, port="5050")
