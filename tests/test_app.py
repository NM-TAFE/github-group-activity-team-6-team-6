import unittest
import app

class TestApp(unittest.TestCase):
    def setUp(self):
        # .testing is a flag for Flask to know the app is in test mode
        app.app.testing = True
        self.client = app.app.test_client()
        # Reset global board between tests, this is a requirement of how Flask works
        app.board[:] = [" "] * 9
        app.current_player = "X"

    def test_home_route(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        # optional: check that the board was rendered
        self.assertIn(b"Tic Tac Toe", response.data)
        self.assertIn(b"Current Player: X", response.data)

    def test_no_play_after_win(self):
        self.client.get("/play/0")
        self.client.get("/play/1")
        self.client.get("/play/3")
        self.client.get("/play/4")
        response = self.client.get("/play/4")
        self.assertEqual(302, response.status_code)
        self.assertNotIn(b"Player X wins!", response.data)
        response = self.client.get("/play/6", follow_redirects=True)
        self.assertEqual(200, response.status_code)
        self.assertEqual(['X', 'O', ' ',
                          'X', 'O', ' ',
                          'X', ' ', ' '], app.board)
        # Game is won. Now test that another marker cant be placed.
        self.assertIn(b"Player X wins!", response.data)
        response = self.client.get("/play/7")
        self.assertEqual(['X', 'O', ' ',
                          'X', 'O', ' ',
                          'X', ' ', ' '], app.board)
