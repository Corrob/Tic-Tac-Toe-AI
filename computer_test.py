import unittest
from computer import Computer
from board import Board

class TestComputer(unittest.TestCase):
    WIDTH = 3
    HEIGHT = 3
    def setUp(self):
        self.computer = Computer()
        self.board = Board(self.WIDTH, self.HEIGHT)

    def update_board_to(self, new_board):
        for y in range(0, self.HEIGHT):
            for x in range(0, self.WIDTH):
                tile = new_board[y][x] # Swap to match
                if tile is not '-':
                    self.board.place_tile(tile, x, y)

    def assert_board(self, board, tile, expected_move):
        self.update_board_to(board)
        move = self.computer.get_move(self.board, tile)
        self.assertEqual(move, expected_move)

    def test_win(self):
        self.assert_board(
                [['X', 'O', 'X'],
                 ['X', 'O', 'X'],
                 ['-', '-', 'O']],
                'X', (0, 2))

    def test_stop_loss(self):
        self.assert_board(
                [['X', 'O', 'X'],
                 ['X', '-', 'O'],
                 ['-', '-', 'O']],
                'O', (0, 2))

    def test_beat_trap(self):
        self.update_board_to(
                [['X', '-', '-'],
                 ['-', 'O', '-'],
                 ['-', '-', 'X']])
        move = self.computer.get_move(self.board, 'O')
        self.assertNotEqual(move, (0, 2))
        self.assertNotEqual(move, (2, 0))

if __name__ == "__main__":
    unittest.main()
