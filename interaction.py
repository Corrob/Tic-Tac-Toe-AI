from board import Board

class Interaction:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        # Used to map numbers to locations for the user
        self.number_board = Board(width, height)
        for x in range(0, width):
            for y in range(0, height):
                self.number_board.place_tile(self.x_y_to_number(x, y), x, y)

    def get_move(self, turn, board):
        print("Current board:")
        board.display()
        print("Board locations:")
        self.number_board.display()
        while True:
            move = input("Where would " + str(turn) + " like to move? ")
            move_num = -1
            try:
                move_num = int(move)
                x, y = self.number_to_x_y(move_num)
                if move_num < 0 or move_num > self.width * self.height - 1:
                    print("Must be a proper location number.")
                elif board.is_occupied(x, y):
                    print("That location is already occupied.")
                else:
                    return (x, y)
            except:
                print("Must be a proper location number.")

    def display_winner(self, board, player_won):
        print("Final board:")
        board.display()
        if player_won:
            print("Congratuations! You are the winner! :)")
        else:
            print("Sorry, the computer has bested you. :(")

    def display_cat_game(self, board):
        print("Final board:")
        board.display()
        print("It was a tie (CAT game)! :|")

    def number_to_x_y(self, num):
        return (num % self.width, num // self.width)

    def x_y_to_number(self, x, y):
        return y * self.width + x

