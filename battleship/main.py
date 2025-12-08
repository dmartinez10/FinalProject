"""
Entry point for the Battleship game.

This file creates the Game object and the GUI window.
"""
import tkinter as tk
from game import Game
from gui import BattleshipGUI

def main():
    game = Game(board_size=10)

    root = tk.TK()

    BattleshipGUI(root, game)

    root.mainloop()

if __name__ == "__main__":
    main()
