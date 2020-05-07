from random import shuffle


class Board:
    def __init__(self):
        self.row, self.col = [int(coordinate)
                              for coordinate in input('Enter dimesnions "<x> <y>": ').split()]

        board_values = []

        j = list(range(self.row * self.col // 2))

        for i in range(0, self.row * self.col, 2):
            k = j.pop()
            board_values.append(chr(ord('A') + k))
            board_values.append(chr(ord('A') + k))

        shuffle(board_values)
        self.board = []
        self.solution_board = []
        for i in range(self.row):
            row = []
            blank_row = []
            for j in range(self.col):
                row.append(board_values.pop())
                blank_row.append('*')
            self.solution_board.append(row)
            self.board.append(blank_row)

        self.temp_board = self.solution_board.copy()

    def __str__(self):
        string = ' |'

        for i in range(0, self.col):
            string += str(i) + ' '

        string += '\n_|' + '__' * self.row + "\n"

        for row in range(0, self.row):
            string += str(row) + '|'
            for col in range(0, self.col):
                string += self.board[row][col] + ' '
            string += '\n'

        return string


board = Board()
print(board)
