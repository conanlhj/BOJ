import heapq

INF = int(1e9)
V, E = map(int, input().split())
edges = [[] for _ in range(V + 1)]
dist = [INF] * (V + 1)

start = int(input())

for _ in range(E):
    u, v, c = map(int, input().split())
    edges[u].append((v, c))


def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        d, u = heapq.heappop(q)
        if dist[u] < d:
            continue
        for end, cost in edges[u]:
            c = d + cost
            if c < dist[end]:
                dist[end] = c
                heapq.heappush(q, (c, end))


dijkstra(start)
print(*list(map(lambda x: str(x) if x != INF else "INF", dist[1:])), sep="\n")
