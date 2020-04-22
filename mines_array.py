import sys


def mark(game_map, x, y):
    game_map[x][y] = "M"
    return game_map


def uncover(map_of_mines, game_map, x, y):
    # for i in range(0, len(map_of_mines)):
    #     map_of_mines[i] = int(map_of_mines[i])

    if map_of_mines[x][y] == 9:
        print("KABLAM\nYou lost")
        for j in range(len(map_of_mines)):
            for i in range(len(map_of_mines[j])):
                print(map_of_mines[i][j], end=' ')
                print()
            sys.exit()
    elif map_of_mines[x][y] == 0:
        game_map[x][y] = str(0)

        if x != 0 and game_map[x - 1][y] == "█":
            uncover(map_of_mines, game_map, x - 1, y)
        if x != 0 and y != 0 and game_map[x - 1][y - 1] == "█":
            uncover(map_of_mines, game_map, x - 1, y - 1)
        if x != 0 and y != 9 and game_map[x - 1][y + 1] == "█":
            uncover(map_of_mines, game_map, x - 1, y + 1)
        if y != 9 and game_map[x][y + 1] == "█":
            uncover(map_of_mines, game_map, x, y + 1)
        if x != 9 and y != 0 and game_map[x + 1][y - 1] == "█":
            uncover(map_of_mines, game_map, x + 1, y - 1)
        if x != 9 and game_map[x + 1][y] == "█":
            uncover(map_of_mines, game_map, x + 1, y)
        if x != 9 and y != 9 and game_map[x + 1][y + 1] == "█":
            uncover(map_of_mines, game_map, x + 1, y + 1)
        if y != 0 and game_map[x][y - 1] == "█":
            uncover(map_of_mines, game_map, x, y - 1)

    else:
        game_map[x][y] = str(map_of_mines[x][y])
    return game_map


class Square:

    def __init(self, map_of_mines, is_opened, is_marked):
        self.map_of_mines = map_of_mines
        self.is_opened = is_opened
        self.is_marked = is_marked



