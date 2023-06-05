from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
res = [[-1] * M for _ in range(N)]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(sx, sy):
    q = deque([(sx, sy, 0)])
    while q:
        x, y, c = q.popleft()
        for dx, dy in d:
            nx, ny = dx + x, dy + y
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1 and res[nx][ny] == -1:
                res[nx][ny] = c + 1
                q.append((nx, ny, c + 1))


for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            bfs(i, j)
            res[i][j] = 0
        elif arr[i][j] == 0:
            res[i][j] = 0
print(*[" ".join(map(str, _)) for _ in res], sep="\n")
