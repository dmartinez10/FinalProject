"""
Board and Ship classes for Battleship game.

- Ship: stores length, coordinates, and hit positions.
- Board: stores a grid, list of ships, and handles shots.
"""

import random

class Ship:

    def __init__(self, length):
        self.length = length
        self.coordinates = []
        self.hits = []

    def place(self, coords):
        """Save the positions where this ship is placed"""
        self.coordinates = coords


    def register_hit(self, row, col):
        """Mark a position as hit if it belongs to this ship."""
        if (row, col) in self.coordinates and (row, col) not in self.hits:
            self.hits.append((row, col))

    def is_sunk(self):
        """Return True if every coordinate for this ship has been hit."""
        for pos in self.coordinates:
            if pos not in self.hits:
                return False
        return True

class Board:
    """Represents a Battleship board with a 2D grid and ships."""

    EMPTY = 0
    SHIP = 1
    HIT = 2
    MISS = 3

    def __init__(self, size=10):
        self.size = size
        #2d list (list of rows, each row is a list of units)
        self.grid = [[Board.EMPTY for _ in range(size)] for _ in range(size)]
        self.ships = [] #list of ship objects

    def in_bounds(self, row, col):
        """Return True if (row, col) is a valid cell on the board."""
        if row < 0 or row >= self.size:
            return False
        if col < 0 or col >= self.size:
            return False
        return True
    
    def can_place_ship(self, length, row, col, horizontal):
        """
        Check if we can place a ship of given length starting at (row, col)
        in a straight line horizontally or vertically.
        """
        for i in range(length):
            if horizontal:
                r = row
                c = col + i
            else:
                r = row + i
                c = col
            
            if not self.in_bounds(r, c):
                return False
            
            if self.grid[r][c] != Board.EMPTY:
                #An object is there
                return False
            
        return True

    def place_ship_randomly(self, length):
        """
        Place one ship of a given legnth on a random valid spot
        Returns the ship object
        """
        placed = False

        while not placed:
            horizontal = random.choice([True, False])
            row = random.randint(0, self.size -1)
            col = random.randint(0, self.size -1)

            if self.can_place_ship(length, row, col, horizontal):
                coords = []
                for i in range(length):
                    if horizontal:
                        r = row
                        c = col + i
                    else:
                        r = row + i
                        c = col
                    
                    self.grid[r][c] = Board.SHIP
                    coords.append((r, c))

                new_ship = Ship(length)
                new_ship.place(coords)
                self.ships.append(new_ship)
                placed = True
                return new_ship


    def receive_shot(self, row, col):
        """
        Handle a shot at (row, col)
        Returns:
            "hit" if it hits a ship
            "miss" if it goes in the water
            "already" if the cell was already shot before
        Raises:
            ValueError if the shot is outside the board
        """
        if not self.in_bounds(row, col):
            raise ValueError("Shot out of bounds")
        
        cell = self.grid[row][col]

        # if it already shot here
        if cell == Board.HIT or cell == Board.MISS:
            return "already"
        
        #if it hits a ship
        if cell == Board.SHIP:
            self.grid[row][col] = Board.HIT

            #finds which ship got hit
            for ship in self.ships:
                if (row, col) in ship.coordinates:
                    ship.register_hit(row, col)
                    if ship.is_sunk():
                        return "sunk"
                    else:
                        return "hit"
        
        #otherwise it was water
        if cell == Board.EMPTY:
            self.grid[row][col] = Board.MISS
            return "miss"
    
    def all_ships_sunk(self):
        """Return True if every ship on this board is sunk."""
        for ship in self.ships:
            if not ship.is_sunk():
                return False
        return True
    