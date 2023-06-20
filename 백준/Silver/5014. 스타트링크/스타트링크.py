from collections import deque
F, S, G, U, D = map(int, input().split())
visited = [-1] * (F + 1)
q = deque([S])
visited[S] = 0
while q:
    x = q.popleft()
    for y in [x + U, x - D]:
        if 0 < y <= F and visited[y] == -1:
            visited[y] = visited[x] + 1
            q.append(y)
print(visited[G] if visited[G] != -1 else "use the stairs")