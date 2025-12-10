"""
tkinter gui for battleship game.

- shows two grids: player board (left) and computer board (right)
- player clicks on computer board to fire
- displays simple status messages and high scores
"""

import tkinter as tk
from tkinter import messagebox

from board import Board
from game import Game


class BattleshipGUI:
    """graphical user interface for the battleship game."""

    def __init__(self, root: tk.Tk, game: Game):
        self.root = root
        self.game = game

        self.root.title("battleship - final project")

        # 2d list of buttons for each board
        self.player_buttons: list[list[tk.Button]] = []
        self.computer_buttons: list[list[tk.Button]] = []

        self.status_label: tk.Label | None = None

        self._build_layout()
        self._update_boards()

    def _build_layout(self) -> None:
        """create labels, frames, and all buttons."""
        size = self.game.size

        # title at the top
        title_label = tk.Label(self.root, text="battleship", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=4, pady=10)

        # labels above each board
        player_label = tk.Label(self.root, text="your board")
        player_label.grid(row=1, column=0, padx=10)

        computer_label = tk.Label(self.root, text="computer board")
        computer_label.grid(row=1, column=2, padx=10)

        # frames to hold the grids of buttons
        player_frame = tk.Frame(self.root)
        player_frame.grid(row=2, column=0, padx=10, pady=10)

        computer_frame = tk.Frame(self.root)
        computer_frame.grid(row=2, column=2, padx=10, pady=10)

        # build player board buttons (no click action, just display)
        for r in range(size):
            row_buttons = []
            for c in range(size):
                btn = tk.Button(
                    player_frame,
                    width=2,
                    height=1,
                    text="",
                )
                btn.grid(row=r, column=c)
                row_buttons.append(btn)
            self.player_buttons.append(row_buttons)

        # build computer board buttons (click to fire)
        for r in range(size):
            row_buttons = []
            for c in range(size):
                btn = tk.Button(
                    computer_frame,
                    width=2,
                    height=1,
                    text="",
                    command=lambda row=r, col=c: self.on_computer_cell_click(row, col),
                )
                btn.grid(row=r, column=c)
                row_buttons.append(btn)
            self.computer_buttons.append(row_buttons)

        # status label at bottom
        self.status_label = tk.Label(self.root, text="your turn", anchor="w")
        self.status_label.grid(row=3, column=0, columnspan=4, sticky="w", pady=10, padx=10)

        # high scores button
        high_scores_btn = tk.Button(self.root, text="show high scores", command=self.show_high_scores)
        high_scores_btn.grid(row=4, column=0, columnspan=4, pady=5)

    def _update_boards(self):
        """
        update button text and color based on each board's grid state.

        player board:
            - show ships ("S"), hits ("X"), and misses ("O")
        computer board:
            - only show hits/misses, do not show ships.
        """
        size = self.game.size

        # update player board buttons
        for r in range(size):
            for c in range(size):
                cell = self.game.player_board.grid[r][c]
                btn = self.player_buttons[r][c]

                # default look
                text = ""
                bg = "light blue"

                if cell == Board.SHIP:
                    text = "S"
                    bg = "gray"
                elif cell == Board.HIT:
                    text = "X"
                    bg = "red"
                elif cell == Board.MISS:
                    text = "O"
                    bg = "white"

                btn.config(text=text, bg=bg)

        # update computer board buttons
        for r in range(size):
            for c in range(size):
                cell = self.game.computer_board.grid[r][c]
                btn = self.computer_buttons[r][c]

                # default: hide ships
                text = ""
                bg = "light blue"

                if cell == Board.HIT:
                    text = "X"
                    bg = "red"
                elif cell == Board.MISS:
                    text = "O"
                    bg = "white"
                # if it's a ship or empty, we leave it blank

                btn.config(text=text, bg=bg)

    def on_computer_cell_click(self, row, col):
        """
        handle player clicking on the computer's board.
        """
        # if game already over, just tell the player and stop
        if self.game.game_over:
            messagebox.showinfo("game over", f"game is over, {self.game.winner} already won.")
            return

        # if it's not the player's turn, ignore click
        if not self.game.player_turn:
            if self.status_label:
                self.status_label.config(text="wait, it's not your turn yet.", fg="black")
            return

        # player fires at the chosen cell
        result = self.game.player_fire(row, col)

        # handle result messages
        if result == "invalid":
            messagebox.showwarning("invalid move", "that shot is out of bounds.")
            return
        elif result == "already":
            messagebox.showinfo("already tried", "you already shot there.")
            return
        elif result == "hit":
            if self.status_label:
                self.status_label.config(text="you hit a ship!", fg="green")
        elif result == "sunk":
            if self.status_label:
                self.status_label.config(text="you sunk a ship!", fg="green")
        elif result == "miss":
            if self.status_label:
                self.status_label.config(text="you missed.", fg="black")
        elif result == "game_over":
            # player wins
            self._update_boards()
            if self.status_label:
                self.status_label.config(text="you win!", fg="green")
            messagebox.showinfo("you win", "congrats, you sank all the ships!")
            return

        # update boards after player's move
        self._update_boards()

        # if the game is not over and shot was valid, let computer play next
        if result not in ("invalid", "already", "game_over"):
            # small delay so it feels like turns
            self.root.after(500, self.computer_turn)

    def computer_turn(self):
        """
        let the computer take a shot, then update everything.
        """
        if self.game.game_over:
            return

        row, col, result = self.game.computer_fire()

        # if somehow game already ended
        if result == "game_over":
            self._update_boards()
            if self.status_label:
                self.status_label.config(text="you lost.", fg="red")
            messagebox.showinfo("you lost", "the computer sank all your ships.")
            return

        # build a simple message for what the computer did
        if result == "hit":
            msg = f"computer hit at ({row}, {col})"
            color = "red"
        elif result == "miss":
            msg = f"computer missed at ({row}, {col})"
            color = "black"
        else:
            msg = f"computer fired at ({row}, {col})"
            color = "black"

        if self.status_label:
            self.status_label.config(text=msg, fg=color)

        # update the board after computer's move
        self._update_boards()

    def show_high_scores(self):
        """
        show a simple message box with list of high scores.
        """
        scores = self.game.get_high_scores()

        if not scores:
            messagebox.showinfo("high scores", "no high scores yet.")
            return

        lines = []
        for index, entry in enumerate(scores, start=1):
            shots = entry.get("shots", "?")
            lines.append(f"{index}. {shots} shots")

        message = "\n".join(lines)
        messagebox.showinfo("high scores", message)
