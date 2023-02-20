class BattleField:
    def __init__(self):
        # For data:
        # . = not visible
        # o = no ship on position
        # x = ship on position

        self._data = [["." for j in range(10)] for i in range(10)]
        self._visibility = [[False for j in range(10)] for i in range(10)]

    def get_symbol(self, row, col):
        return self._data[row][col]

    def set_symbol(self, row, col, symbol):
        self._data[row][col] = symbol

    def get_visibility(self, row, col):
        return self._visibility[row][col]

    def set_visibility_true(self, row, col):
        self._visibility[row][col] = True

    @staticmethod
    def check_position(row, col):
        if (row < 10) and (row >= 0) and (col < 10) and (col >= 0):
            return True
        return False

    def __str__(self):
        board = "X  1  2  3  4  5  6  7  8  9  10 \n"

        for i in range(10):
            board += chr(65+i) + "  "
            for j in range(10):
                if self._visibility[i][j]:
                    board += self.get_symbol(i, j) + "  "
                else:
                    board += "." + "  "
            board += "\n"

        return board
