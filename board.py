class Board:
    def __init__(self, size=10):
        self.size = size
        self.cells = [[None for _ in range(size)] for _ in range(size)]

    def place_unit(self, unit, x, y):
        if self.cells[y][x] is None:
            self.cells[y][x] = unit
            return True
        return False

    def move_unit(self, unit, x, y):
        if self.cells[y][x] is None:
            for row in range(self.size):
                for col in range(self.size):
                    if self.cells[row][col] == unit:
                        self.cells[row][col] = None
                        self.cells[y][x] = unit
                        return True
        return False
