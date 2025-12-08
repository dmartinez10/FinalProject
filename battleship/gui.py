"""
Tkinter GUI for Battleship game.

- Shows two grids: player board (left) and computer board (right)
- Player clicks on computer board to fire
- Displays simple status messages and high scores
"""

import tkinter as tk
from tkinter import messagebox

from board import Board
from game import Game

class BattleshipGUI:
    """Graphical user interface for the Battleship game."""

    def __init__(self, root: tk.TK, game: Game):
        self.root = root
        self.game = game

        self.root.title("Battleship - Final Project")

        # 2D list of buttons for each board

        self.player_buttons: list[list[tk.button]] = []
        self.computer_buttons: list[list[tk.button]] = []

        self.status_label: tk.Label | None = None

        self._build_layout()
        self._update_boards()

    def _build_layout(self) -> None:
        """Create labels, frames, and all buttons."""
        # TODO:
        # 1. Title label at top
        # 2. Two labels: "Your Board" and "Computer Board"
        # 3. Two tk.Frame containers for the grids
        # 4. Nested loops to create 10x10 buttons for each grid
        #    - Player buttons: no command
        #    - Computer buttons: command calls on_computer_cell_click(row, col)
        # 5. Status label at bottom
        # 6. Button for "Show High Scores"

        pass

    def _update_boards(self) -> None:
        """
        Update button text and color based on each board's grid state.

        Player board:
            - Show ships (e.g., "S" or grey color)
            - Show hits ("X" red) and misses ("O" white)
        Computer board:
            - Only show hits/misses, do NOT show ships.
        """
        size = self.game.size


        # TODO:
        # Loop over rows and columns for player_board.grid and computer_board.grid
        # Use Board.EMPTY, Board.SHIP, Board.HIT, Board.MISS to decide:
        #   - button text ("" / "S" / "X" / "O")
        #   - background color (optional but nice)

        pass

    def on_computer_cell_click(self, row: int, col: int) -> None:
        """
        Handle player clicking on the computer's board.
        """
        # TODO:
        # 1. If game.game_over: show info box and return
        # 2. If not game.player_turn: show "Wait, not your turn" and return
        # 3. Call result = self.game.player_fire(row, col)
        # 4. Based on result:
        #    - 'invalid': show warning
        #    - 'already': show info
        #    - 'hit' or 'sunk': update status label in green
        #    - 'miss': update status label
        #    - 'game_over': update boards, show win message, update status, return
        # 5. Call self._update_boards()
        # 6. If the shot was valid and not 'game_over':
        #      schedule computer turn with self.root.after(milliseconds, self.computer_turn)

        pass

    def computer_turn(self) -> None:
        """
        Let the computer take a shot, then update everything.
        """
        # TODO:
        # 1. Call row, col, result = self.game.computer_fire()
        # 2. If result == 'game_over':
        #       update boards, show lose message, update status, return
        # 3. Otherwise:
        #       update status label with what happened
        # 4. Call self._update_boards()

        pass

    def show_high_scores(self) -> None:
        """
        Show a simple message box with list of high scores.
        """
        scores = self.game.get_high_scores()

        if not scores:
            messagebox.showinfo("High Scores", "No high schores yet.")
            return
        
        # Build text like:
        # 1. 35 shots
        # 2. 42 shots

        lines = []
        for index, entry in enumerate(scores, start=1):
            shots = entry.get("shots", "?")
            lines.append(f"{index}. {shots} shots")

        message = "\n".join(lines)
        messagebox.showinfo("High Scores", message)