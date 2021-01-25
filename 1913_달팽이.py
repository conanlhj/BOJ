n = int(input())
target = int(input())

board = [[0]*n for i in range(n)]
x, y = 0, 0
dir = (1, 0)

num = n*n
while num > 0:
    board[y][x] = num
    num -= 1
    x += dir[1]
    y += dir[0]
    if y == n:
        x -= dir[1]
        y -= dir[0]
        dir = (0, 1)
        x += dir[1]
        y += dir[0]
    elif x == n:
        x -= dir[1]
        y -= dir[0]
        dir = (-1, 0)
        x += dir[1]
        y += dir[0]
    elif y == -1:
        x -= dir[1]
        y -= dir[0]
        dir = (0, -1)
        x += dir[1]
        y += dir[0]
    elif board[y][x]:
        if dir == (1, 0):
            x -= dir[1]
            y -= dir[0]
            dir = (0, 1)
            x += dir[1]
            y += dir[0]
        elif dir == (0, 1):
            x -= dir[1]
            y -= dir[0]
            dir = (-1, 0)
            x += dir[1]
            y += dir[0]
        elif dir == (-1, 0):
            x -= dir[1]
            y -= dir[0]
            dir = (0, -1)
            x += dir[1]
            y += dir[0]
        elif dir == (0, -1):
            x -= dir[1]
            y -= dir[0]
            dir = (1, 0)
            x += dir[1]
            y += dir[0]
print(*[' '.join(map(str, board[i])) for i in range(n)], sep='\n')
for i in range(n):
    for j in range(n):
        if board[i][j] == target:
            print(i+1, j+1)
