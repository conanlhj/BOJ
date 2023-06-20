from collections import deque

V = int(input())
s, e = map(int, input().split())
G = [[] for _ in range(V + 1)]
for i in range(int(input())):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

visited = [-1] * (V + 1)
visited[s] = 0
q = deque([s])
while q:
    x = q.popleft()
    for y in G[x]:
        if visited[y] == -1:
            visited[y] = visited[x] + 1
            q.append(y)
print(visited[e])