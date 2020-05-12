from tkinter import *


class Checker:
    def __init__(self, color):
        self.color = color
        self.isKinged = False

    def __str__(self):
        if self.color == 'white':
            if self.isKinged:
                return 'W'
            else:
                return 'w'
        elif self.color == 'black':
            if self.isKinged:
                return 'B'
            else:
                return 'b'

    def __repr__(self):
        return str(self)

    def king(self):
        self.isKinged = True

    def moves(self):
        if self.color == self.color.upper():
            coordinates = [(self.row + 1, self.col + 1), (self.row + 1, self.color - 1),
                           (self.row - 1, self.col + 1), (self.row - 1, self.col - 1)]
        elif self.color == 'w':
            coordinates = [(self.row + 1, self.col + 1),
                           (self.row + 1, self.color - 1)]
        else:
            coordinates = [(self.row - 1, self.col + 1),
                           (self.row - 1, self.color - 1)]

        coordinates = [
            coordinate for coordinate in coordinates if Checker.isValidCoordinate(coordinate)]

        return coordinates

    @staticmethod
    def isValidCoordinate(coordinate):
        return 0 <= coordinate[0] < 8 and 0 <= coordinate[1] < 8


class Board:
    def __init__(self):
        self.board = []
        for i in range(8):
            row = []
            for j in range(8):
                if i < 2:
                    row.append(Checker('white'))
                elif i > 5:
                    row.append(Checker('black'))
                else:
                    row.append(' ')
            self.board.append(row)

    def __str__(self):
        return str(self.board)

    def moves(self, row, col):
        coordinates = self.board[row][col].moves()
        coordinates = [
            coordinate for coordinate in coordinates if self.board[coordinate[0]][coordinate[1]] == 0]

        return coordinates


class GUI:
    def __init__(self):
        root = Tk()
        root.grid()

        board = Board()

        buttons = []
        for row in range(8):
            button_row = []
            for col in range(8):
                button_row.append(
                    Button(root, text=str(board.board[row][col])))
                button_row[col].grid(row=row, column=col)
            buttons.append(button_row)

        root.mainloop()


gui = GUI()
