"""program x/o"""
class TicTacGame:
    """game class"""
    #    board=list(range(1,10))
    def __init__(self):
        self.board = list(range(1, 10))

    def show_board(self):
        """show board"""
        for i in range(1, 10, 3):
            print("{0}|{1}|{2}".format(self.board[i-1], self.board[i], self.board[i+1]))

    def validate_input(self, move):
        """check user`s input"""
        move_set = set('123456789')
        if set(move).issubset(move_set) and move != "":
            if self.board[int(move) - 1] != 'x':
                if self.board[int(move) - 1] != 'o':
                    return True
        return False

    def next_move(self, symb):
        """user`s move"""
        self.show_board()
        move = input("Enter your next move (index in table)...\n")
        while self.validate_input(move) is False:
            move = input("An error in index\n")
        self.board[int(move) - 1] = symb
        if self.check_winner() is True:
            return symb

    def board_complete(self):
        """check board complete"""
        for i in self.board:
            if i in range(1, 10):
                return False
        return True

    def start_game(self):
        """game"""
        while True:
            if self.next_move('x') == 'x':
                return 'x'
            if self.board_complete() is True:
                self.show_board()
                return "Nobody"
            if self.next_move('o') == 'o':
                return 'o'

    def check_winner(self):
        """check user`s win"""
        winner_block = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7),
                        (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for i in winner_block:
            if self.board[i[0]] == self.board[i[1]] == self.board[i[2]]:
                return True
        return False

if __name__ == '__main__':
    START_GAME = input("Do you want to start the game? y/n\n")
    while START_GAME != "n":
        if START_GAME == "y":
            GAME = TicTacGame()
            print("'{0}'won!!!".format(GAME.start_game()))
            START_GAME = input("Do you want to start the game? y/n\n")
        else:
            START_GAME = input("invalid character\nEnter y/n symbol\n")
