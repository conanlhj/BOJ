from collections import deque

M, N, H = map(int, input().split())
arr = [[[0] * M for _ in range(N)] for i in range(H)]

for i in range(H):
    for j in range(N):
        arr[i][j] = list(map(int, input().split()))
d = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]


def bfs(h, i, j):
    q = deque()
    q.append((h, i, j))
    while q:
        c, x, y = q.popleft()
        for dc, dx, dy in d:
            nc = c + dc
            nx = x + dx
            ny = y + dy
            if (
                0 <= nc < H
                and 0 <= nx < N
                and 0 <= ny < M
                and (arr[nc][nx][ny] == 0 or arr[nc][nx][ny] > arr[c][x][y] + 1)
            ):
                arr[nc][nx][ny] = arr[c][x][y] + 1
                q.append((nc, nx, ny))


for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 1:
                bfs(i, j, k)


flag = False
max_val = -1
for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 0:
                flag = True
                print(-1)
                break
            elif arr[i][j][k] > 0:
                max_val = max(max_val, arr[i][j][k])
        if flag:
            break
    if flag:
        break
if not flag:
    print(max_val - 1)
