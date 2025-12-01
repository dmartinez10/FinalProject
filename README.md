# FinalProject
This is a simplified version of the classic game Battleship, created as a final project for our class. The game runs in Python and lets the player guess board positions until all hidden ships are sunk.

The project is organized into multiple files so each part of the game is separate and easy to understand.

battleship/
│── main.py       # Runs the game and connects everything
│── board.py      # Handles the game board and ship placement
│── game.py       # Handles player input and hit/miss logic
└── README.md     # Project explanation

How the Game Works:
A board is created (default size: 5x5).
Ships are randomly placed and hidden from the player.
Each turn:
The board is shown (without revealing ship locations)
The player guesses a row and column
The game checks if it’s a hit or a miss
The board updates with “X” for hit, “O” for miss
The game continues until all ships are sunk.

Features:
Random ship placement
Input validation (no invalid rows/columns)
Hit/miss handling
Displayable board
Win detection

How to Run the Game:
Make sure Python is installed.
Then open a terminal inside the project folder and run:
python3 main.py
or on Windows:
python main.py

Team Members
David Martinez
Franky Adame