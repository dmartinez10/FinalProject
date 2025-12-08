"""
Board and Ship classes for Battleship game.

- Ship: stores length, coordinates, and hit positions.
- Board: stores a grid, list of ships, and handles shots.
"""

import random

class Ship:

    def __init__(self, length: int):
        self.length = length
        self.coordinates = []
        self.hits = set()

    def place(self, coords: list[tuple[int, int]]) -> None:
        """
        Save the locations for this ship.
        coords: list of (row, col) positions.
        """
        # TODO: store coords in the attribute

    def register_hit(self, row: int, col: int) -> None:
        """
        Mark a position as hit if it belongs to this ship.
        """
        # TODO:
        # 1. Check if (row, col) is part of this ship
        # 2. If yes, add it to self.hits

    def is_sunk(self) -> bool:
        """
        Return True if every coordinate for this ship has been hit.
        """
        # TODO:
        # Compare set(self.coordinates) and self.hits
        # return True when all coordinates are in hits
        return False  # placeholder

class Board:
    """
    Represents a Battleship board with a 2D grid and ships.
    """

    def __init__(self, size: int = 10):
        self.size = size
        #2d list (list of rows, each row is a list of units)
        self.grid = [[Board.EMPTY for _ in range(size)] for _ in range(size)]
        self.ships: list[Ship] = []

    def in_bounds(self, row: int, col: int) -> bool:
        """Return True if (row, col) is a valid cell on the board."""
        # TODO: check row and col are between 0 and size-1
        return False #placeholder
    
    def can_place_ship(self, length: int, row: int, col: int, horizontal: bool) -> bool:
        """
        Check if we can place a ship of given length starting at (row, col)
        in a straight line horizontally or vertically.
        """
        # TODO:
        # Loop from 0 to length-1
        #   compute r, c depending on horizontal
        #   if out of bounds or grid[r][c] is not EMPTY, return False
        # If loop finishes, return True
        return False  # placeholder

    def place_ship_randomly(self, length: int) -> Ship:
        """
        Randomly place a ship on the board and return the Ship object.

        Uses random module:
        - Choose random orientation (horizontal/vertical)
        - Choose random starting cell
        - Try again until it fits
        """
        # TODO:
        # Use a while True loop
        #   pick horizontal = random.choice([True, False])
        #   pick random row, col
        #   if can_place_ship(...):
        #       build a list of coordinates
        #       mark grid cells as SHIP
        #       create Ship object, call place(coords), append to self.ships
        #       return the ship

        # temporary placeholder so file runs
        raise NotImplementedError("place_ship_randomly is not implemented yet")

    def received_shot(self, row: int, col: int) -> str:
        """
        Apply a shot to the board.

        Returns:
            'hit', 'miss', 'already', or 'sunk'

        Raises:
            ValueError if (row, col) is outside the board.
        """
        # TODO:
        # 1. If out of bounds -> raise ValueError
        # 2. Read current cell = self.grid[row][col]
        # 3. If cell is HIT or MISS -> return 'already'
        # 4. If cell is SHIP:
        #       mark it as HIT
        #       find which ship has this coord, call register_hit
        #       if that ship is_sunk() -> return 'sunk'
        #       else -> return 'hit'
        # 5. If cell is EMPTY:
        #       mark it as MISS
        #       return 'miss'
        return "miss"  # placeholder
    
    def all_ship_sunk(self) -> bool:
        """
        Return True if every ship on this board is sunk.
        """
        # TODO:
        # loop over self.ships and check ship.is_sunk()
        return False  # placeholder
    