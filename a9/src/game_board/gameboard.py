from colorama import Back

class GameBoard:
    def __init__(self):
        self.__game_board = []

        for _ in range(6):
            self.__game_board.append([None]*7)

    def get_board(self):
        return self.__game_board

    def __str__(self):
        string = "╔══╦══╦══╦══╦══╦══╦══╗"
        for i in range(6):
            string += "\n║"
            for j in range(7):
                if self.__game_board[i][j] == 'red':
                    char = Back.RED + '  ' + Back.RESET
                elif self.__game_board[i][j] == 'yellow':
                    char = Back.YELLOW + '  ' + Back.RESET
                else:
                    char = '  '
                string += char + "║"
            if i != 5:
                string += "\n╠══╬══╬══╬══╬══╬══╬══╣"
        string += "\n╚══╩══╩══╩══╩══╩══╩══╝\n 1  2  3  4  5  6  7"
        return string

    def update_board(self,row,col,colour):
        self.__game_board[row][col] = colour
