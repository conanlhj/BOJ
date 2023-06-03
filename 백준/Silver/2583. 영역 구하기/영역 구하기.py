from collections import deque

M, N, K = map(int, input().split())
d = [(1, 0), (-1, 0), (0, -1), (0, 1)]
arr = [[False] * N for _ in range(M)]

for _ in range(K):
    x_, y_, x, y = map(int, input().split())
    for i in range(y_, y):
        for j in range(x_, x):
            arr[i][j] = True

def bfs(sx, sy):
    q = deque([(sx, sy)])
    arr[sx][sy] = True
    r = 0
    while q:
        x, y = q.popleft()
        r += 1
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < M and 0 <= ny < N and not arr[nx][ny]:
                arr[nx][ny] = True
                q.append((nx, ny))
    return r

cnt = 0
result = []
for i in range(M):
    for j in range(N):
        if not arr[i][j]:
            result.append(bfs(i, j))
            cnt += 1
print(cnt)
print(*sorted(result))