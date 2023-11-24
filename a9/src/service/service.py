from src.service.ai import Ai

class Service:
    def __init__(self, gb):
        self.__board = gb

    def check_empty(self,col):
        # -1 = full column
        board = self.__board.get_board()
        for i in range(5, -1, -1):
            if board[i][col] == None:
                return i
        return -1

    def player_move(self,col):
        row = self.check_empty(col)
        if row == -1:
            raise ValueError("Row is full")
        self.__board.update_board(row,col,'red')
        return

    def check_win_condition(self):
        winner = self.check_line()
        if winner == 'red' or winner == 'yellow':
            return winner
        winner = self.check_column()
        if winner == 'red' or winner == 'yellow':
            return winner
        winner = self.check_diag_right()
        if winner == 'red' or winner == 'yellow':
            return winner
        winner = self.check_diag_left()
        if winner == 'red' or winner == 'yellow':
            return winner

    def check_line(self):
        board =  self.__board.get_board()
        for i in range(5,-1,-1):
            for j in range(4):
                if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] != None:
                    return board[i][j]

    def check_column(self):
        board = self.__board.get_board()
        for i in range(5, 2, -1):
            for j in range(7):
                if board[i][j] == board[i - 1][j] == board[i - 2][j] == board[i - 3][j] != None:
                    return board[i][j]



    def check_diag_right(self):
        board = self.__board.get_board()
        for i in range(5, 2, -1):
            for j in range(4):
                if board[i][j] == board[i - 1][j + 1] == board[i - 2][j + 2] == board[i - 3][j + 3] != None:
                    return board[i][j]


    def check_diag_left(self):
        board = self.__board.get_board()
        for i in range(5, 2, -1):
            for j in range(6,2,-1):
                if board[i][j] == board[i - 1][j - 1] == board[i - 2][j - 2] == board[i - 3][j - 3] != None:
                    return board[i][j]

    def ai_move(self):
        ai = Ai(self.__board.get_board())
        col = ai.play()
        row = self.check_empty(col)
        if row == -1:
            self.ai_move()
        self.__board.update_board(row, col, 'yellow')
        del ai

    def get_board(self):
        return self.__board.get_board()

    def __str__(self):
        return str(self.__board)

