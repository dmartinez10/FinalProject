"""
Entry point for the Battleship game.

This file creates the Game object and the GUI window.
"""
import tkinter as tk
from game import Game
from board import Board
from gui import BattleshipGUI

def main():
    root = tk.Tk()
    game = Game(size=5)
    gui = BattleshipGUI(root, game)
    root.mainloop()

if __name__ == "__main__":
    main()

