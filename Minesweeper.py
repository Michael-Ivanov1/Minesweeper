import mines_array
import random
import os


game = mines_array.MineField(10)

print("Welcome to Minesweeper!")
print()
print(input("Press Enter to Continue"))

os.system("clear")

while not game.game_over:
    game.play()








# hide loop
# while True:
#     # array of the mines
#     arr_mines = [[0 for i in range(10)] for j in range(10)]
#
#     # array to be printed during the game
#     arr_game = [["█" for a in range(10)] for b in range(10)]
#
#     # place mines at random position
#     for i in range(10):
#         ran_X = random.randint(0, 9)
#         ran_Y = random.randint(0, 9)
#         arr_mines[ran_X][ran_Y] = 9
#
#     count = 0
#     for number in arr_mines:
#         if number == 9:
#             count += 1
#
#     # Checks the position of mines and fills the numbers around them.
#     for i in range(len(arr_mines)):
#         for j in range(len(arr_mines[i])):
#             if arr_mines[i][j] != 9:
#                 mines_array.c_mines(i, j, arr_mines)
#
#     print("Welcome to Minesweeper!")
#     print()
#
#     print(input("Press Enter to Continue"))
#
#     # placeholder to have a loop
#     mark_count = 0
#     block_count = 0
#
#     while True:
#         mines_array.print_mines(arr_game)
#
#         print("Entering C clears a spot and M marks it.")
#         ask = input("Enter a command: ").upper()
#
#         try:
#             x, y = input("Enter the coordinates: ").split()
#         except ValueError:
#             x, y = input("Enter a coordinate PAIR: ").split()
#
#         os.system("clear")
#         print(x + " " + y)
#         print()
#
#         if ask == "C":
#             mines_array.uncover(arr_mines, arr_game, int(x), int(y))
#
#         elif ask == "M":
#             mines_array.mark(arr_game, int(x), int(y))
#             mark_count += 1
#
#     print("You won!")
