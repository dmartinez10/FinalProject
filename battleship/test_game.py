# test the game.py to see if its working
from game import Game

g = Game(size=5)

print("Player board:")
for row in g.player_board.grid:
    print(row)

print("\nComputer board (for testing only):")
for row in g.computer_board.grid:
    print(row)

print("\nPlayer fires at (0, 0):")
print("Result:", g.player_fire(0, 0))

print("\nComputer turn:")
print(g.computer_fire())

print("\nWinner (if any):", g.winner)
print("Game over:", g.game_over)
