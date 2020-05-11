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
        coordinates = [coordinate for coordinate in coordinates if  # TODO]


class Board:
    def __init__(self):
        self.board= []
        for i in range(8):
            row= []
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


print(Board())
