import sys
import random


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


class Square:
    # upon creating the individual square, these variables are set

    def __init__(self):
        self.is_mine = False
        self.is_marked = False
        self.is_covered = True
        self.surrounding_mines = 0

    def set_mine_true(self):
        self.is_mine = True

    def mark(self):
        self.is_marked = True
        self.is_covered = False

    def print(self):
        if self.is_covered:
            return "█"
        elif self.is_marked:
            return "M"
        elif self.is_mine and not self.is_covered:
            return "@"
        else:
            return self.surrounding_mines

    def print_all(self):
        if self.is_mine:
            return "@"
        else:
            return self.surrounding_mines


class MineField:

    def __init__(self, size):
        self.square_array = [[Square() for x in range(size)] for y in range(size)]
        self.size = size
        self.mine_count = 0
        self.has_won = False
        self.set_mines()
        self.game_over = False

    def uncover(self, x, y):
        self.square_array[x][y].is_covered = False

        if self.square_array[x][y].is_mine:
            print("KABLAM!\nYou lost")
            self.print_all()

        elif self.square_array[x][y].surrounding_mines == 0:

            for a in [x - 1, x, x + 1]:
                for b in [y - 1, y, y + 1]:
                    if a in range(self.size) and b in range(self.size):
                        if self.square_array[a][b].is_covered:
                            self.uncover(a, b)

    def play(self):

        self.print()

        print("Entering C clears a spot and M marks it.")
        string = input("Enter a command: ").upper()

        print()
        try:
            x, y = input("Enter the coordinates: ").split()
        except ValueError:
            x, y = input("Enter a coordinate PAIR: ").split()

        if string == "C":
            self.uncover(int(x), int(y))
        elif string == "M":
            self.square_array[int(x)][int(y)].mark()
        else:
            print("please enter a command")

        game_count = self.size * self.size
        for x in range(self.size):
            for y in range(self.size):
                if not self.square_array[x][y].is_covered or self.square_array[x][y].is_marked:
                    game_count -= 1
        if game_count == self.mine_count:
            self.print_all()
            print("Congratulations, you won!")

    def print(self):
        for x in range(self.size):
            print(x, end=' ')
        print()
        print()
        for j in range(self.size):
            for i in range(self.size):
                print(self.square_array[i][j].print(), end=' ')
            print(" " + str(j))

    def set_mines(self):
        for i in range(10):

            x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)

            self.square_array[x][y].is_mine = True
            self.mine_count += 1

            for a in [x - 1, x, x + 1]:
                for b in [y - 1, y, y + 1]:
                    if a in range(self.size) and b in range(self.size):
                        self.square_array[a][b].surrounding_mines += 1

    def print_all(self):
        for x in range(self.size):
            print(x, end=' ')
        print()
        print()
        for j in range(self.size):
            for i in range(self.size):
                print(self.square_array[i][j].print_all(), end=' ')
            print(" " + str(j))
        self.game_over = True
