import heapq

N, M, X = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, c = map(int, input().split())
    G[u].append((v, c))


def dijkstra(start):
    h = []
    dist = [int(1e9)] * (N + 1)
    dist[start] = 0
    heapq.heappush(h, (0, start))
    while h:
        c, u = heapq.heappop(h)
        if dist[u] < c:
            continue
        for v, cc in G[u]:
            if dist[v] > c + cc:
                dist[v] = c + cc
                heapq.heappush(h, (dist[v], v))
    return dist


dist_x = dijkstra(X)
max_val = -1
for i in range(1, N + 1):
    if i != X:
        max_val = max(max_val, dijkstra(i)[X] + dist_x[i])
print(max_val)
