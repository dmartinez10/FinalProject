# test the board.py to see if its working
from board import Board

b = Board(5)
b.place_ship_randomly(3)
print("Grid after placing one ship:")
for row in b.grid:
    print(row)

print("Shot result:", b.receive_shot(0, 0))