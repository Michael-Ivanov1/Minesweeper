import sys


def c_mines(x, y, mines):
    count = 0
    c = [x - 1, x, x + 1]
    d = [y - 1, y, y + 1]

    for a in c:
        for b in d:
            if a in range(10) and b in range(10):
                if mines[a][b] == 9:
                    count += 1

    mines[x][y] = count


def mark(game_map, x, y):
    game_map[x][y] = "M"
    return game_map


def uncover(map_of_mines, game_map, x, y):

    if map_of_mines[x][y] == 9:
        print("KABLAM!\nYou lost")
        for j in range(len(map_of_mines)):
            for i in range(len(map_of_mines[j])):
                print(map_of_mines[i][j], end=' ')
                print()
            sys.exit()

    elif map_of_mines[x][y] == 0:
        game_map[x][y] = str(0)

        c = [x - 1, x, x + 1]
        d = [y - 1, y, y + 1]

        for a in c:
            for b in d:
                if a in range(len(map_of_mines)) and b in range(len(map_of_mines)):
                    if game_map[a][b] == "█":
                        uncover(map_of_mines, game_map, a, b)

    else:
        game_map[x][y] = str(map_of_mines[x][y])
    return game_map


def print_mines(arr_game):
    print("0 1 2 3 4 5 6 7 8 9")
    print()

    for j in range(len(arr_game)):
        for i in range(len(arr_game[j])):
            print(arr_game[i][j], end=' ')
        print(" " + str(j))


class Square:

    def __init(self, map_of_mines, is_opened, is_marked):
        self.map_of_mines = map_of_mines
        self.is_opened = is_opened
        self.is_marked = is_marked



