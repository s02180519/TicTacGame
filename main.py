"""program x/o"""
class TicTacGame:
    """game class"""
    #    board=list(range(1,10))
    def __init__(self):
        self.board = list(range(1, 10))

    def show_board(self):
        """show board"""
        for i in range(1, 10, 3):
            print(self.board[i - 1], '|', self.board[i], '|', self.board[i + 1], '\n')

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
                return None
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
    GAME = TicTacGame()
    print("'", GAME.start_game(), "' won!!!")
