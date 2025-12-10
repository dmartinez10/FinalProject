# Battleship – Final Project

A simple Battleship Game built in Python using Tkinter and object-oriented programming

## How to Play
- Your board is on the left. It shows your ships ('S'), hits ('X'), and misses ('O')
- The computer's board is on the right. It only shows hits and misses
- Click a square on the computer's board to fire
- After your move, the computer fires back immediately 
- The game ends when either you or the computer sinks all ships

## Features
- Two boards displayed side-by-side
- Turn-based gameplay (player -> computer -> player)
- Winner/loser pop-up messages
- High-score tracking (fewest shots to win)

## How to Run
In the project folder:
```bash
python3 main.py

board.py - this contains board grid, hits/misses, ship storage
game.py - game, flow, turns, win logic, high scores
gui.py - Tkinter interface and button interactions
main.py - starts the game 

Created by: David Martinez and Franky Adame