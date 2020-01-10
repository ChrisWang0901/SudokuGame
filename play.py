from board import *

b = Board(level=3)
print("Initial Board")
b.print_board()
b.solve()
print("Solved Board")
b.print_board()
