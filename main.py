from board import Board
from interaction import Interaction
from computer import Computer
import sys

def main(player_first = True):
    WIDTH = 3
    HEIGHT = 3

    board = Board(WIDTH, HEIGHT)
    interaction = Interaction(WIDTH, HEIGHT)
    computer = Computer()
    turn = 'X'
    if player_first:
        computer_tile = 'O'
    else:
        computer_tile = 'X'

    while board.get_winner() is None and not board.is_cat_game():
        if turn == computer_tile:
            x, y = computer.get_move(board, computer_tile)
            board.place_tile(turn, x, y)
        else:
            x, y = interaction.get_move(turn, board)
            board.place_tile(turn, x, y)
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    if board.is_cat_game():
        interaction.display_cat_game(board)
    else:
        interaction.display_winner(board, board.get_winner() != computer_tile)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        main()
    else:
        main(False)
