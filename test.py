"""test main.py"""

import unittest
from main import TicTacGame


class MyTestCase(unittest.TestCase):
    """Test class"""

    def setUp(self):
        self.game = TicTacGame()

    def test_validate_input(self):
        """test function validate_input"""
        self.assertEqual(self.game.validate_input('10'), False)
        self.assertEqual(self.game.validate_input('1'), True)
        self.assertEqual(self.game.validate_input('9'), True)
        self.assertEqual(self.game.validate_input("g"), False)

        self.game.board[0] = "x"
        self.assertEqual(self.game.validate_input('0'), False)
        self.assertEqual(self.game.validate_input(""), False)

    def test_check_winner(self):
        """test function check_winner"""
        test_win_block = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                          (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for i in test_win_block:
            self.game.board[i[0]], self.game.board[i[1]], self.game.board[i[2]] = 'x', 'x', 'x'
            self.assertEqual(self.game.check_winner(), True)
            self.game.board = list(range(1, 10))
        for i in test_win_block:
            self.game.board[i[0]], self.game.board[i[1]], self.game.board[i[2]] = 'x', 'o', 'x'
            self.assertEqual(self.game.check_winner(), False)
            self.game.board = list(range(1, 10))

    def test_board_complete(self):
        """test function board_complete"""
        for i in range(0, 9):
            if i in (0, 1, 4, 6):
                self.game.board[i] = 'x'
            else:
                self.game.board[i] = 'o'
        self.assertEqual(self.game.board_complete(), True)
        self.game.board[3] = 4
        self.assertEqual(self.game.board_complete(), False)


if __name__ == '__main__':
    unittest.main()
