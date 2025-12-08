# create_board(size) -> returns a 2D list (list of lists)
# place_ships(board, num_ships) -> puts ships on the board
# display_board(board, reveal=False) -> prints the board

class Board:
    def __init__(self, size=10):
        #1. save size
        #2. create grid(list of lists) filled with "~"
        pass

    def place_ship(self, row, col, lenght, direction):
        #mark some cells as "S"
        pass

    def shoot(self, row, col):
        #check whats at that cell and update it
        #return "hit", "miss", or "already"
        pass

    def display(self):
        #print the grid row by row
        pass