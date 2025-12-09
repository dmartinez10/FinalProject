"""
Game class for Battleship.

Handles:
- Two boards (player and computer)
- Turn order
- Firing logic
- Win/lose conditions
- High score saving/loading (extra credit)
"""

import random
import json
from board import Board


class Game:
    """Core game logic for Battleship."""

    def __init__(self, size=10):
        self.size = size

        #board for player and computer
        self.player_board = Board(size)
        self.computer_board = Board(size)

        # standard ship lengths
        self.ship_lengths = [5, 4, 3, 3, 2]

        # track whos turn it is
        self.player_turn = True
        #tracks shots for high score
        self.player_shots = 0
        self.computer_shots = 0

        # game state
        self.game_over = False
        self.winner = None #'player' or 'computer'

        # place ship for both boards
        self.place_all_ships()

    def place_all_ships(self):
        """Place ships for both player and computer (currently random)."""
        for length in self.ship_lengths:
            self.player_board.place_ship_randomly(length)
            self.computer_board.place_ship_randomly(length)

#players turn
    def player_fire(self, row, col):
        """
        Player fires at a cell on the computer's board.

        Returns:
            'hit', 'miss', 'already', 'invalid', 'sunk','game_over' if this shot wins the game,
        """
        if self.game_over:
            return "game_over"
        
        try:
            result = self.computer_board.receive_shot(row, col)
        except ValueError:
            return "invalid"
        
        #count valid new shots
        if result not in ("already", "invalid"):
            self.player_shots += 1
        
        #checks if computer lost
        if self.computer_board.all_ships_sunk():
            self.game_over = True
            self.winner = "player"
            self._save_high_score(self.player_shots)
            return "game_over"
        
        #if the shot was invalid, switch turns
        if result not in ("already", "invalid"):
            self.player_turn = False

        return result
    
    #computer turn
    def computer_fire(self):
        """
        Computer randomly fires at the player's board.
        Returns: (row, col, result)
        """
        if self.game_over:
            return (-1, -1, "game_over")
        
        while True:
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)

            cell = self.player_board.grid[row][col]

            if cell == Board.HIT or cell == Board.MISS:
                continue #if already shot here, pick again

            try:
                result = self.player_board.receive_shot(row, col)
            except ValueError:
                continue

            break

        self.computer_shots += 1

        #checks if the player lost
        if self.player_board.all_ships_sunk():
            self.game_over = True
            self.winner = "computer"
            return (row, col, "game_over")
        
        self.player_turn = True

        return (row, col, result)
    
#EXTRA CREDIT section HIGH SCORE

    def _load_high_scores(self):
        """Loads saved scores from highscores.json"""
        try:
            with open("highscores.json", "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        
    def _save_high_score(self, shots):
        """saves a new score and keeps only the best 10"""
        scores = self._load_scores()
        scores.append({"shots": shots})

        #sorts, fewer shots = better
        scores.sort(key=lambda s: s["shots"])

        #keep best 10
        scores = scores[:10]

        with open("highscores.json", "w") as f:
            json.dump(scores, f, indent=2)

    def get_high_scores(self):
        """allows GUI to read high score"""
        return self._load_high_scores