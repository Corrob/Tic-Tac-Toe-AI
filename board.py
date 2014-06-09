class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = []
        for x in range(0, width):
            self.tiles.append([])
            for y in range(0, height):
                self.tiles[x].append(' ')

    def display(self):
        for y in range(0, self.height):
            if y > 0:
                self.print_horizontal_seperator()
            print(' ', end='')
            for x in range(0, self.width):
                if x > 0:
                    print(' | ', end='')
                print(self.tiles[x][y], end='')
        print()

    def print_horizontal_seperator(self):
        print()
        for i in range(0, self.width):
            if i != 0:
                print('----', end='')
            else:
                print('---', end='')
        print()

    def place_tile(self, tile, x, y):
        self.tiles[x][y] = tile

    def is_occupied(self, x, y):
        return self.tiles[x][y] != ' '

    def is_cat_game(self):
        for x in range(0, self.width):
            for y in range(0, self.height):
                if self.tiles[x][y] == ' ':
                    return False
        return True

    def get_winner(self):
        rows = self.check_rows()
        if rows is not None:
            return rows
        cols = self.check_cols()
        if cols is not None:
            return cols
        diags = self.check_diags()
        if diags is not None:
            return diags

        return None

    def check_rows(self):
        for y in range(0, self.height):
            current_tile = self.tiles[0][y]
            if current_tile == ' ':
                continue
            all_same = True
            for x in range(1, self.width):
                if self.tiles[x][y] != current_tile:
                    all_same = False
            if all_same:
                return current_tile
        return None

    def check_cols(self):
        for x in range(0, self.width):
            current_tile = self.tiles[x][0]
            if current_tile == ' ':
                break
            all_same = True
            for y in range(1, self.height):
                if self.tiles[x][y] != current_tile:
                    all_same = False
            if all_same:
                return current_tile
        return None

    def check_diags(self):
        current_tile = self.tiles[0][0]
        all_same = True
        if current_tile != ' ':
            for x in range(1, min(self.width, self.height)):
                if self.tiles[x][x] != current_tile:
                    all_same = False
            if all_same:
                return current_tile
        current_tile = self.tiles[self.width - 1][0]
        all_same = True
        if current_tile != ' ':
            for x in range(1, min(self.width, self.height)):
                if self.tiles[self.width - x - 1][x] != current_tile:
                    all_same = False
            if all_same:
                return current_tile
        return None

    def clone(self):
        b = Board(self.width, self.height)
        for x in range(0, self.width):
            for y in range(0, self.height):
                b.place_tile(self.tiles[x][y], x, y)
        return b
