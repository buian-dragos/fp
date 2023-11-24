import random as r

class Ai:
    def __init__(self, gb):
        self.__board = gb

    def check(self,colour):
        col = self.check_column(colour)
        if col != None:
            return col
        col = self.check_line(colour)
        if col != None:
            return col
        col = self.check_diag_left(colour)
        if col != None:
            return col
        col = self.check_diag_right(colour)
        if col != None:
            return col


    def check_line(self,colour):
        for i in range(5, -1, -1):
            for j in range(4):
                if self.__board[i][j] == self.__board[i][j + 1] == self.__board[i][j + 2] == colour and self.__board[i][j + 3] == None:
                    if i == 5:
                        return j + 3
                    elif self.__board[i + 1][j + 3] != None:
                            return j + 3
                if self.__board[i][j] == self.__board[i][j + 1] == self.__board[i][j + 3] == colour and self.__board[i][j + 2] == None:
                    if i == 5:
                        return j + 2
                    elif self.__board[i + 1][j + 3] != None:
                            return j + 2
                if self.__board[i][j] == self.__board[i][j + 3] == self.__board[i][j + 2] == colour and self.__board[i][j + 1] == None:
                    if i == 5:
                        return j + 1
                    elif self.__board[i + 1][j + 3] != None:
                            return j + 1
                if self.__board[i][j + 3] == self.__board[i][j + 1] == self.__board[i][j + 2] == colour and self.__board[i][j] == None:
                    if i == 5:
                        return j
                    elif self.__board[i + 1][j + 3] != None:
                            return j


    def check_column(self,colour):
        for i in range(5, 2, -1):
            for j in range(7):
                if self.__board[i][j] == self.__board[i - 1][j] == self.__board[i - 2][j] == colour and self.__board[i - 3][j] == None:
                    return j


    def check_diag_right(self,colour):
        for i in range(5, 2, -1):
            for j in range(4):
                if self.__board[i][j] == self.__board[i - 1][j + 1] == self.__board[i - 2][j + 2] == colour and self.__board[i - 3][j + 3] == None:
                    if i == 5:
                        return j + 3
                    elif self.__board[i + 1][j + 3] != None:
                            return j + 3
                if self.__board[i][j] == self.__board[i - 1][j + 1] == self.__board[i - 3][j + 3] == colour and self.__board[i - 2][j + 2] == None:
                    if i == 5:
                        return j + 2
                    elif self.__board[i + 1][j + 2] != None:
                            return j + 2
                if self.__board[i][j] == self.__board[i - 3][j + 3] == self.__board[i - 2][j + 2] == colour and self.__board[i - 1][j + 1] == None:
                    if i == 5:
                        return j + 1
                    elif self.__board[i + 1][j + 1] != None:
                            return j + 1
                if self.__board[i - 3][j + 3] == self.__board[i - 1][j + 1] == self.__board[i - 2][j + 2] == colour and self.__board[i][j] == None:
                    if i == 5:
                        return j
                    elif self.__board[i + 1][j] != None:
                            return j
    def check_diag_left(self,colour):
        for i in range(5, 2, -1):
            for j in range(6, 2, -1):
                if self.__board[i][j] == self.__board[i - 1][j - 1] == self.__board[i - 2][j - 2] == colour and self.__board[i - 3][j - 3] == None:
                    if self.__board[i - 2][j - 3] != None:
                        return j - 3
                if self.__board[i][j] == self.__board[i - 1][j - 1] == self.__board[i - 3][j - 3] == colour and self.__board[i - 2][j - 2] == None:
                    if self.__board[i - 1][j - 2] != None:
                        return j - 2
                if self.__board[i][j] == self.__board[i - 2][j - 2] == self.__board[i - 3][j - 3] == colour and self.__board[i - 1][j - 1] == None:
                    if self.__board[i][j - 1] != None:
                        return j - 1
                if self.__board[i - 1][j - 1] == self.__board[i - 2][j - 2] == self.__board[i - 3][j - 3] == colour and self.__board[i][j] == None:
                    if i == 5:
                        return j
                    elif self.__board[i + 1][j - 1] != None:
                        return j


    def count(self):
        ltr_max, ltr_col = self.count_line_ltr()
        rtl_max, rtl_col = self.count_line_rtl()
        clm_max, clm_col = self.count_column()
        if ltr_max > rtl_max and ltr_max > clm_max:
            return ltr_col
        elif rtl_max > ltr_max and rtl_max > clm_max:
            return rtl_col
        elif clm_max > rtl_max and clm_max > ltr_max:
            return clm_col
        else:
            return -1

    def count_line_ltr(self):
        mx = 0
        col = -1
        for i in range(5,-1,-1):
            for j in range(4):
                if self.__board[i][j] == 'yellow':
                    if self.__board[i][j + 1] == self.__board[i][j + 2] == self.__board[i][j + 3] == None:
                        ct = 1
                    if self.__board[i][j + 1] == 'yellow' and self.__board[i][j + 2] == self.__board[i][j + 3] == None:
                        ct = 2
                        if ct > mx:
                            mx = ct
                            col = j + 2
                    if self.__board[i][j + 2] == 'yellow' and self.__board[i][j + 1] == self.__board[i][j + 3] == None:
                        ct = 2
                        if ct > mx:
                            mx = ct
                            col = j + 1
                    if self.__board[i][j + 3] == 'yellow' and self.__board[i][j + 2] == self.__board[i][j + 1] == None:
                        ct = 2
                        if ct > mx:
                            mx = ct
                            col = j + 1
                    if self.__board[i][j + 1] == None and self.__board[i][j + 2] == self.__board[i][j + 3] == 'yellow':
                        ct = 3
                        if ct > mx:
                            mx = ct
                            col = j + 1
                    if self.__board[i][j + 2] == None and self.__board[i][j + 1] == self.__board[i][j + 3] == 'yellow':
                        ct = 2
                        if ct > mx:
                            mx = ct
                            col = j + 2
                    if self.__board[i][j + 3] == None and self.__board[i][j + 2] == self.__board[i][j + 1] == 'yellow':
                        ct = 2
                        if ct > mx:
                            mx = ct
                            col = j + 3
        return mx, col

    def count_line_rtl(self):
        mx = 0
        col = -1
        for i in range(5,-1,-1):
            for j in range(6,3,-1):
                if self.__board[i][j] == 'yellow':
                    if self.__board[i][j] == 'yellow':
                        if self.__board[i][j - 1] == self.__board[i][j - 2] == self.__board[i][j - 3] == None:
                            ct = 1
                        if self.__board[i][j - 1] == 'yellow' and self.__board[i][j - 2] == self.__board[i][j - 3] == None:
                            ct = 2
                            if ct > mx:
                                mx = ct
                                col = j - 2
                        if self.__board[i][j - 2] == 'yellow' and self.__board[i][j - 1] == self.__board[i][j - 3] == None:
                            ct = 2
                            if ct > mx:
                                mx = ct
                                col = j - 1
                        if self.__board[i][j - 3] == 'yellow' and self.__board[i][j - 2] == self.__board[i][j - 1] == None:
                            ct = 2
                            if ct > mx:
                                mx = ct
                                col = j - 1
                        if self.__board[i][j - 1] == None and self.__board[i][j - 2] == self.__board[i][j - 3] == 'yellow':
                            ct = 3
                            if ct > mx:
                                mx = ct
                                col = j - 1
                        if self.__board[i][j - 2] == None and self.__board[i][j - 1] == self.__board[i][j - 3] == 'yellow':
                            ct = 2
                            if ct > mx:
                                mx = ct
                                col = j - 2
                        if self.__board[i][j - 3] == None and self.__board[i][j - 2] == self.__board[i][j - 1] == 'yellow':
                            ct = 2
                            if ct > mx:
                                mx = ct
                                col = j - 3
        return mx, col

    def count_column(self):
        mx = 0
        col = -1
        for i in range(5, 3, -1):
            for j in range(7):
                if self.__board[i][j] == 'yellow' and self.__board[i - 1][j] == None:
                    ct = 1
                    if ct > mx:
                        mx = ct
                        col = j
                elif self.__board[i][j] == self.__board[i - 1][j] == 'yellow' and self.__board[i-2][j] == None:
                    ct = 2
                    if ct > mx:
                        mx = ct
                        col = j
        return mx, col

    def play(self):
        col = self.check('yellow')
        if col != None:
            return col
        col = self.check('red')
        if col != None:
            return col
        col = self.count()
        if col == -1:
            return r.randint(0,6)
        return col
