import mines_array
import check_mines
import random
import os

# array of the mines
arr_mines = [[0 for i in range(10)] for j in range(10)]

# array to be printed during the game
arr_game = [["█" for a in range(10)] for b in range(10)]


# place mines at random position
for i in range(10):
    ran_X = random.randint(0, 9)
    ran_Y = random.randint(0, 9)
    arr_mines[ran_X][ran_Y] = 9

for i in range(len(arr_mines)):
    for j in range(len(arr_mines[i])):
        if arr_mines[i][j] != 9:
            check_mines.c_mines(i, j, arr_mines)



print("Welcome to Minesweeper!")
print()

print("0 1 2 3 4 5 6 7 8 9")

for j in range(len(arr_game)):
    for i in range(len(arr_game[j])):
        print(arr_game[i][j], end=' ')
    print(" " + str(j))

print(input("Press Enter to Continue"))

# placeholder to have a loop
game_placeholder = 100
while game_placeholder > 20:
    print("Entering C clears a spot and M marks it.")
    ask = input("Enter a command: ").upper()

    try:
        x, y = input("Enter the coordinates: ").split()
    except ValueError:
        x, y = input("Enter a coordinate PAIR: ").split()

    os.system("clear")
    print(x + " " + y)
    print()

    if ask == "C":
        mines_array.uncover(arr_mines, arr_game, int(x), int(y))
    elif ask == "M":
        mines_array.mark(arr_game, int(x), int(y))

    print("0 1 2 3 4 5 6 7 8 9")
    print()

    for j in range(len(arr_game)):
        for i in range(len(arr_game[j])):
            print(arr_game[i][j], end=' ')
        print(" " + str(j))
#    print(input("Press Enter to Continue"))
    game_placeholder -= 1

print("You won!")
