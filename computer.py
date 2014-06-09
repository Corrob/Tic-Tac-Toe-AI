class Computer:
    MAX_MOVES = 9
    def get_move(self, board, tile):
        move, score = self.get_move_recursion(board, tile, 0, True)
        return move

    def get_move_recursion(self, board, tile, depth, good_turn):
        winner = board.get_winner()
        if winner is not None:
            return (None, self.get_score(winner == tile, good_turn, depth))
        elif board.is_cat_game():
            return (None, 0)
        best_move = None
        best_score = None
        for x in range(0, board.width):
            for y in range(0, board.height):
                if not board.is_occupied(x, y):
                    new_board = board.clone()
                    new_board.place_tile(tile, x, y)
                    move, score = self.get_move_recursion(new_board, self.swap_tile(tile), depth + 1, not good_turn)
                    if best_score is None:
                        best_move = (x, y)
                        best_score = score
                        continue
                    if good_turn and score >= best_score:
                        best_move = (x, y)
                        best_score = score
                    if not good_turn and score <= best_score:
                        best_move = (x, y)
                        best_score = score
        return (best_move, best_score)

    def swap_tile(self, tile):
        if tile == 'X':
            return 'O'
        else:
            return 'X'

    def get_score(self, won, good_turn, depth):
        if (won and good_turn) or (not won and not good_turn):
            return self.MAX_MOVES - depth
        else:
            return depth - self.MAX_MOVES


