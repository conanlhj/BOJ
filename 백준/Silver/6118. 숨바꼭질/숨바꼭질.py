from collections import deque

N, M = map(int, input().split())
dist = [-1] * (N + 1)
edges = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)
dist[1] = 0

q = deque([1])
while q:
    u = q.popleft()
    for v in edges[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            q.append(v)

max_dist = max(dist)
print(dist.index(max_dist), max_dist, dist.count(max_dist))
