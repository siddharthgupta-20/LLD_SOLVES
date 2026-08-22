from user import User
from board import Board
class Game:
    def __init__(self):
        self.board = Board()
        self.players = []
        self.make_move_flag = True


    def add_player(self,name, symbol):
        u = User(name,symbol)
        self.players.append(u)

    def make_move(self, name, x,y):
        if self.make_move_flag:
            self.board.player1.append((x,y))
            self.make_move_flag = False
        else:
            self.board.player2.append((x,y))
            self.make_move_flag = True
        self.board.check_state()
        

    def decide(self):
        if self.board.status == "win":
            return (self.board.status, self.players[self.board.winner].name)
        else:
            return self.board.status 