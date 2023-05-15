import heapq

N, E = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(E):
    u, v, c = map(int, input().split())
    G[u].append((v, c))
    G[v].append((u, c))
v1, v2 = map(int, input().split())

def dijkstra(start):
    h = []
    dist = [int(1e9)] * (N + 1)
    dist[start] = 0
    heapq.heappush(h, (0, start))
    while h:
        prev_cost, prev_v = heapq.heappop(h)
        if prev_cost > dist[prev_v]:
            continue
        for curr_v, curr_cost in G[prev_v]:
            if dist[curr_v] > prev_cost + curr_cost:
                dist[curr_v] = prev_cost + curr_cost
                heapq.heappush(h, (dist[curr_v], curr_v))
    return dist

dist_v1 = dijkstra(v1)
dist_v2 = dijkstra(v2)

ans_1 = dist_v1[1] + dist_v1[v2] + dist_v2[N]
ans_2 = dist_v2[1] + dist_v2[v1] + dist_v1[N]

print(min(ans_1, ans_2) if ans_1 < int(1e9) or ans_2 < int(1e9) else -1)