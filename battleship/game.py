"""
Game class for Battleship.

Handles:
- Two boards (player and computer)
- Turn order
- Firing logic
- Win/lose conditions
- High score saving/loading (extra credit)
"""

from pathlib import Path
import json
import random

from board import Board

HIGHSCORE_FILE = Path("highscores.json")

class Game:
    """Core game logic for Battleship."""

    def __init__(self, board_size: int = 10):
        self.size = board_size
        self.player_board = Board(board_size)
        self.computer_board = Board(board_size)

        # ship sizes adjustment
        self.ship_lengths = [5, 4, 3, 3, 2]

        # turn tracking
        self.player_turn = True
        self.player_shots = 0
        self.computer_shots = 0

        # game state
        self.game_over = False
        self.winner: str | None = None #'player' or 'computer'

        # place ship for both boards
    def place_all_ships(self) -> None:
        """Place ships for both player and computer (currently random)."""
        # TODO:
        # for each length in self.ship_lengths:
        #   call place_ship_randomly(length) on both boards
        pass

    def player_fire(self, row: int, col: int) -> str:
        """
        Player fires at a cell on the computer's board.

        Returns:
            'hit', 'miss', 'already', 'sunk',
            'game_over' if this shot wins the game,
            or 'invalid' if the click was outside the board.

        This is where we do exception handling for invalid shots.
        """
        if self.game_over:
            return "game_over"
        
        try:
            result = self.computer_board.receive_shot(row, col)
        except ValueError:
            # out of bounds shot
            return "invalid"
        
        # TODO:
        # If result is not 'already' or 'invalid', increase self.player_shots
        # Check if computer_board.all_ships_sunk() -> if yes:
        #    set game_over, set winner = "player"
        #    call self._save_high_score(self.player_shots)
        #    return 'game_over'
        # If the shot was new (not 'already'), change self.player_turn = False

        return result # placeholder, update when add logic
    
    def computer_fire(self) -> tuple[int, int, str]:
        """
        Computer randomly fires at the player's board.

        Returns:
            (row, col, result)
        """
        if self.game_over:
            return -1, -1, "game_over"
        

        # TODO:
        # Repeat until you find a cell that is not already HIT/MISS:
        #   row = random.randint(0, self.size - 1)
        #   col = random.randint(0, self.size - 1)
        #   call player_board.receive_shot(row, col)
        #
        # Increase self.computer_shots
        # If all player's ships sunk -> set game_over and winner = "computer"
        # Change self.player_turn = True when done

        return -1, -1, "miss" #placeholder
    
#####EXTRA CREDIT HIGH SCORE METHOD

    def _load_high_scores(self) -> list[dict]:
        """
        Load high scores from JSON file.

        Uses exception handling so the game doesn't crash
        if the file is missing or corrupted.
        """
        if not HIGHSCORE_FILE.exist():
            return []
        
        try:
            with HIGHSCORE_FILE.open("r", encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, OSError):
            # bad file or read error -> just pretend no scores exist
            return []
        
        # ensure its a list of dicts
        if isinstance(data, list):
            return data
        return []
    
    def _save_high_score(self, shots: int) -> None:
        """
        Save a new high score entry.

        We store a list of dictionaries like:
        [
          {"shots": 35},
          {"shots": 40}
        ]
        """
        
        scores = self._load_high_scores()
        scores.append({"shots": shots})

        # sort scores so fewer shots is better
        scores.sort(key=lambda entry: entry.get("shots", 9999))

        # keep top 10
        scores = scores[:10]

        try:
            with HIGHSCORE_FILE.open("w", encoding="utf-8") as f:
                json.dump(scores, f, indent=2)
        except OSError:
            # cant write file? ignore, game should not crash
            pass

    def _get_high_scores(self) -> list[dict]:
        """Return high scores (used by GUI to display them)."""
        return self._load_high_scores