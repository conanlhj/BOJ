from collections import deque
N, M = map(int, input().split())
campus = [input() for _ in range(N)]
visited = [[False] * M for _ in range(N)]
ans = 0
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def bfs(sx, sy):
    global ans
    q = deque([(sx, sy)])
    visited[sx][sy] = True
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < N
                and 0 <= ny < M
                and not visited[nx][ny]
                and campus[nx][ny] != "X"
            ):
                if campus[nx][ny] == "P":
                    ans += 1

                visited[nx][ny] = True
                q.append((nx, ny))
for i in range(N):
    for j in range(M):
        if campus[i][j] == "I":
            bfs(i, j)
            print(ans if ans > 0 else "TT")
            exit()
