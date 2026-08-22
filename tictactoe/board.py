class Board:
    def __init__(self):
        self.status = "play"
        self.winner = -1
        self.player1 = []
        self.player2 = []

    def check_state(self):
        if len(self.player1) + len(self.player2) == 9:
            self.status = "draw"

        if Board.check_win(self.player1):
            self.status = "win"
            self.winner = 0
        elif Board.check_win(self.player2):
            self.status = "win"
            self.winner = 1
        else:
            pass
        return  
    
    def check_win(l):
        # check horizontal
        for i in range(3):
            count = 0
            count2 = 0
            for j in range(3):
                if (i,j) in l :
                    count+=1
                if (j,l) in l :
                    count2+=1
            if count == 3 or count2 == 3:
                return True

        # check diagonal
        count1 = 0
        count2 = 0
        for i in range(3):
            if (i,i) in l:
                count1 +=1
            if (3-i-1,i) in l:
                count2 +=1
        if count1==3 or count2==3:
            return True
                