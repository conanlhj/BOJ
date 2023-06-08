from collections import deque
cnt = 1
INF = int(1e9)
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
while True:
    n = int(input())
    if n == 0: break
    arr = [list(map(int, input().split())) for _ in range(n)]
    dist = [[INF] * n for _ in range(n)]
    q = deque([(0, 0)])
    dist[0][0] = arr[0][0]
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx, ny = dx + x, dy + y
            if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] > dist[x][y] + arr[nx][ny]:
                dist[nx][ny] = dist[x][y] + arr[nx][ny]
                q.append((nx, ny))

    print(f"Problem {cnt}: {dist[-1][-1]}")
    cnt += 1