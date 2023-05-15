import heapq as h

N = int(input())
M = int(input())
G = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, c = map(int, input().split())
    G[u].append((v, c))

start, end = map(int, input().split())

q = []
h.heappush(q, (0, start))
dist = [int(1e9)] * (N+1)
dist[start] = 0

while q:
    curr_cost, curr = h.heappop(q)
    
    if dist[curr] < curr_cost:
        continue
    
    for u, cost in G[curr]:
        if dist[u] > curr_cost + cost:
            dist[u] = curr_cost + cost
            h.heappush(q, (dist[u], u))

print(dist[end])