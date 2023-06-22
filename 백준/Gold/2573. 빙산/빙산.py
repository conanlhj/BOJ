from collections import deque
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
D = [(1, 0), (-1, 0), (0, 1), (0, -1)]
ans = 0
def bfs(sx, sy):
    q = deque([(sx, sy)])
    visited[sx][sy] = True
    while q:
        x, y = q.popleft()
        for dx, dy in D:
            nx = dx + x
            ny = dy + y
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and arr[nx][ny] != 0:
                visited[nx][ny] = True
                q.append((nx, ny))
while True:
    visited = [[False] * M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0 and not visited[i][j]:
                bfs(i, j)
                cnt += 1
    if cnt >= 2:
        print(ans)
        break
    if cnt == 0:
        print(0)
        break
    new_arr = [[i for i in j] for j in arr]
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                tmp = 0
                for dx, dy in D:
                    nx = i + dx
                    ny = j + dy
                    if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
                        tmp += 1
                new_arr[i][j] -= tmp
                if new_arr[i][j] < 0:
                    new_arr[i][j] = 0
    arr = new_arr
    ans += 1