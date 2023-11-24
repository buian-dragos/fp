class Ui:
    def __init__(self, serv):
        self.__service = serv

    def play(self):
        # player =  red; AI = yellow
        while True:
            print(str(self.__service))
            while True:
                col = input("Choose column: ")
                if col.isdigit():
                    col = int(col) - 1
                    break
                else:
                    print("Invalid input")
            try:
                self.__service.player_move(col)
            except ValueError as error:
                print(str(error))
            else:
                winner = self.__service.check_win_condition()
                if winner != None:
                    print(str(self.__service))
                    print(f"{winner} wins!")
                    return
                self.__service.ai_move()
                winner = self.__service.check_win_condition()
                if winner != None:
                    print(str(self.__service))
                    print(f"{winner} wins!")
                    return
