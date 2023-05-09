from collections import deque

N = int(input())
M = [input() for _ in range(N)]
d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
v = [[False] * N for _ in range(N)]


def bfs(x, y, c):
    q = deque([(x, y)])
    while q:
        i, j = q.popleft()
        for dx, dy in d:
            nx = i + dx
            ny = j + dy
            if 0 <= nx < N and 0 <= ny < N and not v[nx][ny] and M[nx][ny] in c:
                q.append((nx, ny))
                v[nx][ny] = True


cnt = 0
for i in range(N):
    for j in range(N):
        if not v[i][j]:
            bfs(i, j, M[i][j])
            cnt += 1
print(cnt, end=" ")


v = [[False] * N for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(N):
        if not v[i][j] and M[i][j] == "B":
            bfs(i, j, M[i][j])
            cnt += 1
        elif not v[i][j]:
            bfs(i, j, "RG")
            cnt += 1
print(cnt, end=" ")
