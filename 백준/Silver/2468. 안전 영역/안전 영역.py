from collections import deque
n = int(input())
min_, max_ = 101, 0
arr = []
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for _ in range(n):
    tmp = list(map(int, input().split()))
    min_ = min(min_, *tmp)
    max_ = max(max_, *tmp)
    arr.append(tmp)
def bfs(sx, sy, h):
    q = deque([(sx, sy)])
    visited[sx][sy] = True
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] > h and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
ans = 1
for h in range(min_, max_):
    visited = [[False] * n for _ in range(n)]
    tmp = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > h and not visited[i][j]:
                tmp += 1
                bfs(i, j, h)
    ans = max(ans, tmp)
print(ans)