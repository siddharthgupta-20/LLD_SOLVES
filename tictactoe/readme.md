
# REQUIREMENTS:

. 3X3 grid
. 3 in a straight     -> WIN!! WOOHOOO!!!
. all space filled    -> DRAW!!  NO EYE FOR AN EYE!
. alternating moves : one move at a time
. validate moves (should be in bound, should be at an open space etc).

## CLASSES:

* ### Board: (state of the game)
    - coordinates
    - filled {}
    - empty  {}
    - Check_state()  -> check if the current state is of either continue, win or draw
    - Update_board() -> for a player to add their move to the board.

* ### Player: ( only 2 player)
    - username
    - user_symbol
    - play_move(x,y) -> to send out your move

* ### Game: (orchestrator, idk the spelling)
    - add_player
    - init_board
    - ask board to update, shout to the player who win or declare draw
    - ask player to move 