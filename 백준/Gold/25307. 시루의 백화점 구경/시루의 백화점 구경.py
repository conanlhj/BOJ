from collections import deque

N, M, K = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
mannequins = []
d = [[1, 0], [-1, 0], [0, 1], [0, -1]]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 3:
            mannequins.append((i, j))
            arr[i][j] = 1
        elif arr[i][j] == 4:
            start = (i, j)


def bfs_mann(mann):
    
    q = deque()
    for i, j in mann:
        q.append((i, j, 0))
        visited[i][j] = True
    
    while q:
        x, y, c = q.popleft()
        if c == K:
            continue
        
        for dx, dy in d:
            nx = dx + x
            ny = dy + y
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, c+1))
                arr[nx][ny] = 1


bfs_mann(mannequins)
visited = [[False] * M for _ in range(N)]

def bfs(startx, starty):
    q = deque([(startx, starty, 0)])
    visited[startx][starty] = True
    while q:
        sx, sy, c = q.popleft()
        if arr[sx][sy] == 2:
            return c
        for dx, dy in d:
            nx = dx + sx
            ny = dy + sy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and arr[nx][ny] != 1:
                visited[nx][ny] = True
                q.append((nx, ny, c+1))
    return -1

print(bfs(start[0], start[1]))