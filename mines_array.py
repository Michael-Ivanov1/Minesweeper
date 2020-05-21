import random

import pygame
import pygame_gui

pygame.init()
clock = pygame.time.Clock()
font = pygame.font.SysFont("Sans", 20)

scale = 32
shift = 100

window_width = 900
window_height = 900


def t(file):
    return pygame.transform.scale(pygame.image.load(file), (scale, scale))


m = "Minesweeper_images/"
numbers = [t(m + "Minesweeper_uncovered_tile.png"), t(m + "Minesweeper_1.png"),
           t(m + "Minesweeper_2.png"), t(m + "Minesweeper_3.png"),
           t(m + "Minesweeper_4.png"), t(m + "Minesweeper_5.png"),
           t(m + "Minesweeper_6.png"), t(m + "Minesweeper_7.png"),
           t(m + "Minesweeper_8.png")]
mines = [t(m + "Minesweeper_Mine.png"), t(m + "Minesweeper_Blewup_Mine.png"),
         t(m + "Minesweeper_X_Mine.png")]
flag = t(m + "Minesweeper_flag.png")
tile = t(m + "Minesweeper_Tile.png")

background = pygame.display.set_mode((window_width, window_height))
background.fill((100, 80, 150))
pygame.display.set_caption("Minesweeper")

manager = pygame_gui.UIManager((window_width, window_height))


class DifficultyButton:
    def __init__(self, difficulty, position):
        self.button = pygame_gui.elements.UIButton(pygame.Rect(position, (90, 45)), difficulty, manager)


buttons = [DifficultyButton("Easy", (50, 100)).button, DifficultyButton("Medium", (50, 150)).button,
           DifficultyButton("Difficult", (50, 200)).button]
dif = {"Easy": (10, 10, 12), "Medium": (15, 15, 50), "Difficult": (20, 20, 75)}


class Square:
    # upon creating the individual square, these variables are set

    def __init__(self, x, y):

        self.is_mine, self.is_marked, self.is_covered = False, False, True
        self.position = (x * scale + shift + 100, y * scale + shift)

        self.surrounding_mines = 0
        self.image, self.covered = numbers[0], tile

    def show_value(self):
        if self.is_covered:
            return self.covered
        else:
            return self.image

    def set_mine(self):
        self.is_mine = True
        self.image = mines[0]

    def mark(self):
        if self.is_marked:
            self.is_marked = False
            self.image = tile
        else:
            self.is_marked = True
            self.image = flag
        self.is_covered = False


class MineField:

    def __init__(self, size_x, size_y, mine_count, difficulty):
        self.square_array = [[Square(x, y) for x in range(20)] for y in range(20)]
        self.size_x, self.size_y = size_x, size_y

        self.mine_count = mine_count
        self.set_minefield()
        self.game_over, self.first_click = False, True

        self.difficulty = difficulty

    def reset(self, size_x, size_y, mine_count, difficulty):
        self.square_array = [[Square(x, y) for x in range(size_x)] for y in range(size_y)]
        self.size_x, self.size_y = size_x, size_y

        self.mine_count = mine_count
        self.set_minefield()
        self.game_over, self.first_click = False, True

        self.difficulty = difficulty

    def uncover(self, x, y):
        self.square_array[x][y].is_covered = False

        if self.square_array[x][y].is_mine:
            self.square_array[x][y].image = mines[1]

            # Uncover the entire board

            for a in range(self.size_x):
                for b in range(self.size_y):
                    self.square_array[a][b].is_covered = False

        elif self.square_array[x][y].surrounding_mines == 0:

            # Cycles through every number around the clicked zero and clears it

            for a in [x - 1, x, x + 1]:
                for b in [y - 1, y, y + 1]:
                    if a in range(self.size_x) and b in range(self.size_y):
                        if self.square_array[a][b].is_covered:
                            self.uncover(a, b)

    def shuffle(self, x, y):

        # if the first click is not on a zero, the board shuffles until that clicked position is a zero

        while not self.square_array[x][y].surrounding_mines == 0:
            self.reset(dif[self.difficulty][0], dif[self.difficulty][1], dif[self.difficulty][2], self.difficulty)

        self.uncover(x, y)
        self.first_click = False

    def set_minefield(self):
        total_mines = 0
        while total_mines < self.mine_count:

            x, y = random.randint(0, self.size_x - 1), random.randint(0, self.size_y - 1)

            if not self.square_array[x][y].is_mine:

                total_mines += 1

                # Add one to every spot around a mine

                for a in [x - 1, x, x + 1]:
                    for b in [y - 1, y, y + 1]:
                        if a in range(self.size_x) and b in range(self.size_y) and not self.square_array[a][b].is_mine:
                            self.square_array[a][b].surrounding_mines += 1
                            self.square_array[a][b].image = numbers[self.square_array[a][b].surrounding_mines]

                # Because a, b is x, y, I have to set the original position to a mine and display a mine image

                self.square_array[x][y].set_mine()

    def pygame_play(self):

        while not self.game_over:
            time_delta = clock.tick(60) / 1000.0

            my, mx = pygame.mouse.get_pos()

            click_x, click_y = (mx - shift) // scale, (my - shift - 100) // scale

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if event.button == 1:       # Left Click
                        if click_x in range(self.size_x) and click_y in range(self.size_y):
                            if self.first_click and not self.square_array[click_x][click_y].surrounding_mines == 0:
                                self.shuffle(click_x, click_y)

                            else:
                                self.uncover(click_x, click_y)

                    elif event.button == 3:     # Right Click
                        if click_x in range(self.size_x) and click_y in range(self.size_y):
                            self.square_array[click_x][click_y].mark()

                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:     # Syntax for Pygame_Gui
                        if event.ui_element == buttons[0]:
                            background.fill((100, 80, 150))

                            self.reset(dif["Easy"][0], dif["Easy"][1], dif["Easy"][2], "Easy")

                        if event.ui_element == buttons[1]:
                            background.fill((100, 80, 150))

                            self.reset(dif["Medium"][0], dif["Medium"][1], dif["Medium"][2], "Medium")

                        if event.ui_element == buttons[2]:
                            background.fill((100, 80, 150))

                            self.reset(dif["Difficult"][0], dif["Difficult"][1], dif["Difficult"][2], "Difficult")

                manager.process_events(event)

            for x in range(self.size_x):
                for y in range(self.size_y):
                    background.blit(self.square_array[x][y].show_value(), self.square_array[x][y].position)

            manager.update(time_delta)

            manager.draw_ui(background)
            pygame.display.update()
