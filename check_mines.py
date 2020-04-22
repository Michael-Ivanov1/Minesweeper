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
