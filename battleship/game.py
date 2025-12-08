# get_player_move() -> asks user for row and column, returns them
# is_hit(board, row, col) -> returns True if there is a ship
# update_board(board, row, col, hit) -> marks X or O
# ships_remaining(board) -> counts how many 'S' are left

from board import Board

class Game:
    def __init__(self):
        #create boards for each player
        self.player1_board = Board()
        self.player2_board = Board()
        #make something to track whos turn it is

    def start(self):
        #main game loop lives here
        #1. show board
        #2. ask for input
        #3. call shoot()
        #4. check win condition
        pass