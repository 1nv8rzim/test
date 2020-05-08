from random import shuffle
from copy import deepcopy


class Board:

    @staticmethod
    def get_coordinate(string):
        return [int(coordinate)for coordinate in input(string).split()]

    def __init__(self):
        while True:
            self.row, self.col = Board.get_coordinate(
                "Enter board dimensions: ")
            if (self.row * self.col) % 2 != 0:
                print("Number of Cards is Odd. Try New Dimensions.")
            else:
                break

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

        self.temp_board = deepcopy(self.board)

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

    def reveal(self):
        print(self)
        while True:
            first_card = Board.get_coordinate("First Card: ")
            if self.board[first_card[0]][first_card[1]] == '*':
                break
            else:
                print('Card Already Revealed. Try Again.')

        self.board[first_card[0]][first_card[1]
                                  ] = self.solution_board[first_card[0]][first_card[1]]
        print(self)

        while True:
            second_card = Board.get_coordinate("Second Card: ")
            if self.board[second_card[0]][second_card[1]] == '*':
                break
            else:
                print('Card Already Revealed. Try Again.')

        self.board[second_card[0]][second_card[1]
                                   ] = self.solution_board[second_card[0]][second_card[1]]
        print(self)

        if self.solution_board[first_card[0]][first_card[1]] == self.solution_board[second_card[0]][second_card[1]]:
            print("Match!")
            self.temp_board = deepcopy(self.board)
            print(self)
        else:
            print("Mismatch")
            self.board = deepcopy(self.temp_board)

    def game_over(self):
        for row in self.board:
            if '*' in row:
                return False
        return True


board = Board()
while True:
    board.reveal()
    if board.game_over():
        print('You Win!')
        break
