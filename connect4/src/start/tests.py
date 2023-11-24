from src.game_board.gameboard import GameBoard
from src.service.service import Service
from src.ui.ui import Ui
import unittest

class Tests(unittest.TestCase):
    def test_move(self):
        gb = GameBoard()
        serv = Service(gb)

        serv.player_move(0)
        board = serv.get_board()
        self.assertEqual(board[5][0],'red')

        serv.ai_move()

        string = str(serv)
        self.assertEqual(len(string), 339)

    def test_full(self):
        gb = GameBoard()
        serv = Service(gb)

        serv.player_move(0)
        serv.player_move(0)
        serv.player_move(0)
        serv.player_move(0)
        serv.player_move(0)
        serv.player_move(0)

        self.assertEqual(serv.check_empty(0),-1)

        try:
            serv.player_move(0)
        except ValueError:
            pass

    def test_ai1(self):
        gb = GameBoard()
        serv = Service(gb)
        serv.player_move(0)
        serv.player_move(1)
        serv.player_move(2)

        serv.ai_move()

    def test_ai2(self):
        gb = GameBoard()
        serv = Service(gb)
        serv.player_move(0)
        serv.player_move(1)
        serv.player_move(3)

        serv.ai_move()

    def test_ai3(self):
        gb = GameBoard()
        serv = Service(gb)
        serv.player_move(0)
        serv.player_move(2)
        serv.player_move(3)

        serv.ai_move()

    def test_ai4(self):
        gb = GameBoard()
        serv = Service(gb)
        serv.player_move(0)
        serv.player_move(0)
        serv.player_move(0)

        serv.ai_move()

    def test_win1(self):
        gb = GameBoard()
        serv = Service(gb)

        win = serv.check_win_condition()
        self.assertIsNone(win)

    def test_win2(self):
        gb = GameBoard()
        serv = Service(gb)

        serv.player_move(0)
        serv.player_move(0)
        serv.player_move(0)
        serv.player_move(0)

        win = serv.check_win_condition()
        self.assertIsNotNone(win)

    def test_win3(self):
        gb = GameBoard()
        serv = Service(gb)

        serv.player_move(0)
        serv.player_move(1)
        serv.player_move(2)
        serv.player_move(3)

        win = serv.check_win_condition()
        self.assertIsNotNone(win)

    def test_win4(self):
        gb = GameBoard()
        serv = Service(gb)

        serv.player_move(0)
        serv.player_move(1)
        serv.player_move(1)
        serv.player_move(2)
        serv.ai_move()
        serv.player_move(2)
        serv.player_move(2)
        serv.player_move(3)
        serv.player_move(3)
        serv.player_move(3)

        win = serv.check_win_condition()
        self.assertIsNotNone(win)

    def test_win5(self):
        gb = GameBoard()
        serv = Service(gb)

        serv.player_move(3)
        serv.player_move(2)
        serv.player_move(2)
        serv.player_move(1)
        serv.ai_move()
        serv.player_move(1)
        serv.player_move(1)
        serv.player_move(0)
        serv.player_move(0)
        serv.player_move(0)

        win = serv.check_win_condition()
        self.assertIsNotNone(win)

