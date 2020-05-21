import mines_array
import os

a = mines_array.dif["Easy"]
game = mines_array.MineField(a[0], a[1], a[2], "Easy")

print("Welcome to Minesweeper!")
print()

game.pygame_play()
