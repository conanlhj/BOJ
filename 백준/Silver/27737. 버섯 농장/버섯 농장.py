from collections import deque
from math import ceil

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(sx, sy):
    q = deque([(sx, sy)])
    visited[sx][sy] = True
    cnt = 1
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx = dx + x
            ny = dy + y
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny] == 0:
                visited[nx][ny] = True
                q.append((nx, ny))
                cnt += 1
    return cnt


res = M
for i in range(N):
    for j in range(N):
        if arr[i][j] == 0 and not visited[i][j]:
            cnt = bfs(i, j)
            res -= ceil(cnt / K)

if res < 0 or res == M:
    print("IMPOSSIBLE")
else:
    print("POSSIBLE")
    print(res)