from hangman_visuals import hangman_progression


class Board ():
    def answer_string(self):
        string = ''
        for letter in self.answer:
            if letter == ' ':
                string += ' '
            elif letter in self.guessed:
                string += letter
            else:
                string += '_'
        return string

    def __str__(self):
        return self.hangman[len(self.wrong)] + "\nWrong: " + str(self.wrong) + "\nGuessed: " + str(self.guessed) + "\n" + self.answer_string()

    def __init__(self, answer):
        self.answer = answer
        self.guessed = []
        self.wrong = []
        self.hangman = hangman_progression

    def guess(self, letter):
        self.guessed += letter
        if letter not in self.answer:
            self.wrong += letter

    def game_over(self):
        return len(self.wrong) == 6 or '_' not in self.answer_string()

    def win(self):
        return '_' not in self.answer_string()

    def win_board(self):
        return self.hangman[len(self.wrong)] + "\nWrong: " + str(self.wrong) + "\nGuessed: " + str(self.guessed) + "\n" + self.answer


while True:
    board = Board(input("Enter answer:").upper().strip())
    print(end="\n\n\n\n\n\n\n\n\n\n")
    while True:
        print(board)
        guess = ''
        while guess == '':
            guess = input("Guess letter:").upper().strip()
        if guess == board.answer:
            board.win_board()
            print("You win!")
            break
        elif guess in board.guessed:
            print("Letter already guessed, try again")
        else:
            board.guess(guess[0])
        if board.game_over():
            if board.win():
                print(board.win_board())
                print("You win!")
                break
            else:
                print(board.win_board())
                print("You Lose")
                break
