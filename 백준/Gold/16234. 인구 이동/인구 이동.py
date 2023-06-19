from collections import deque
t2o = lambda x, y: N*x + y
o2t = lambda x: (x//N, x%N)
N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

def bfs(sx, sy):
    q = deque([(sx, sy)])
    visited[sx][sy] = True
    total = arr[sx][sy]
    union = [(sx, sy)]
    while q:
        x, y = q.popleft()
        n = t2o(x, y)
        for next in G[n]:
            nx, ny = o2t(next)
            if not visited[nx][ny]:
                union.append((nx, ny))
                q.append((nx, ny))
                total += arr[nx][ny]
                visited[nx][ny] = True
    
    new_p = total // len(union)
    for x, y in union:
        arr[x][y] = new_p

while True:
    G = [[] for _ in range(N*N)]
    visited = [[False] * N for _ in range(N)]
    flag = True
    
    for i in range(N):
        for j in range(N):
            if j + 1 < N and L <= abs(arr[i][j] - arr[i][j+1]) <= R:
                G[t2o(i, j)].append(t2o(i, j+1))
                G[t2o(i, j+1)].append(t2o(i, j))
                flag = False
            if i + 1 < N and L <= abs(arr[i][j] - arr[i+1][j]) <= R:
                G[t2o(i, j)].append(t2o(i+1, j))
                G[t2o(i+1, j)].append(t2o(i, j))
                flag = False
    
    if flag:
        print(ans)
        break
    
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(i, j)
    
    ans += 1