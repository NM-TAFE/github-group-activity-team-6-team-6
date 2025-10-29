import unittest
import app

class TestApp(unittest.TestCase):
    def setUp(self):
        # .testing is a flag for Flask to know the app is in test mode
        app.app.testing = True
        self.client = app.app.test_client()
        # Reset global board between tests, this is a requirement of how Flask works
        app.board[:] = [" "] * 9
        app.current_player = None

    def test_home_route(self):
        response = self.client.get("/play")
        self.assertEqual(response.status_code, 200)
        # optional: check that the board was rendered
        self.assertIn(b"Tic Tac Toe", response.data)
        self.assertTrue(
            b"Player X starts first" in response.data
            or b"Player O starts first" in response.data
            or b"It's: X's turn!" in response.data
            or b"It's: O's turn!" in response.data,
            "Expected player message not found."
        )

    def test_no_play_after_win(self):
        # start random first player
        self.client.get("/play")
        self.client.get("/play/0")
        self.client.get("/play/1")
        self.client.get("/play/3")
        self.client.get("/play/4")
        response = self.client.get("/play/6", follow_redirects=True)
        self.assertEqual(200, response.status_code)
        winner = app.check_winner()
        self.assertIn(winner, ['X', 'O']), "expected a winner (X or O)"
        # verify the win message is in the response 
        self.assertIn(f"Player {winner} wins!".encode(), response.data)
        #take a snapshot of the current board state
        board_snapshot = app.board.copy()
        # try to play again - board should not change
        self.client.get("/play/7")
        self.assertEqual(board_snapshot, app.board, "Board changed after game was won")