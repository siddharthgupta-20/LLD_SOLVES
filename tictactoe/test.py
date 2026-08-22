from game import Game
from board import Board
from user import User

game = Game()

game.add_player("adam","X")
game.add_player("eve","O")

game.make_move("adam",1,1)
print(game.decide())
game.make_move("eve",2,1)
print(game.decide())
game.make_move("adam",0,0)
print(game.decide())
game.make_move("eve",0,1)
print(game.decide())

game.make_move("adam",2,2)
print(game.decide())



