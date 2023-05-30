def check_box(x, y, n):
    sx = x // 3 * 3
    sy = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if sudoku[sx + i][sy + j] == n:
                return False
    return True


def check_row(x, n):
    for i in sudoku[x]:
        if i == n:
            return False
    return True


def check_col(y, n):
    for i in range(9):
        if sudoku[i][y] == n:
            return False
    return True


def bk(idx):
    if idx == len(blank):
        print(*[" ".join(map(str, i)) for i in sudoku], sep="\n")
        exit()
    x, y = blank[idx]
    for i in range(1, 10):
        if check_box(x, y, i) and check_row(x, i) and check_col(y, i):
            sudoku[x][y] = i
            bk(idx + 1)
    sudoku[x][y] = 0


blank = []
sudoku = [list(map(int, input().split())) for _ in range(9)]
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blank.append((i, j))

bk(0)
