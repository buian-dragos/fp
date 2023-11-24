from src.game_board.gameboard import GameBoard
from src.service.service import Service
from src.ui.ui import Ui


if __name__ == '__main__':
    gb = GameBoard()
    serv = Service(gb)
    ui = Ui(serv)

    ui.play()