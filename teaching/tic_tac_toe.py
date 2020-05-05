class Board ():
    def __init__ (self):
        self.board = [[' ', ' ', ' '],[' ', ' ', ' '], [' ', ' ', ' ']]
        
    def __str__ (self):
        temp = ''
        for row in self.board:
            for col in row:
                temp += col + '|'
            temp = temp[:-1] + "\n"
            temp += "-----\n"
        temp = temp[:-6]
        return temp
    
    def make_move(self, player, row, col):
        self.board[row][col] = player
        
    def game_over (self):
        for row in self.board:
            if  row[0] != ' ' and row[0] == row[1] == row[2]:
                return True
        for i in range(0,3):
            if self.board[0][i] != ' ' and self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return True
        if self.board[0][0] != ' ' and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return True
        if self.board[2][0] != ' ' and self.board[2][0] == self.board[1][1] == self.board[0][2]:
            return True
        return False
    
    def tie (self):
        for row in self.board:
            for col in row:
                if col == ' ':
                    return False
        return True     
        
board = Board()
print(board)
while (True):
    move = input("X make a move: ")
    move = move.split(' ')
    board.make_move('X', int(move[0]), int(move[1]))
    print(board)
    if (board.game_over()):
        print("X wins!")
        break
    if (board.tie()):
        print("Tie!")
        break
    move = input("O make a move: ")
    move = move.split(' ')
    board.make_move('O', int(move[0]), int(move[1]))
    print(board)
    if (board.game_over()):
        print("O wins!")
        break
    if (board.tie()):
        print("Tie!")
        break
