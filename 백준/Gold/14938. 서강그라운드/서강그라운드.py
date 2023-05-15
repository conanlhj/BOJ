n, m, r = map(int, input().split())
G = [[int(1e9)] * (n + 1) for _ in range(n + 1)]
for i in range(n + 1):
    G[i][i] = 0

items = [0] + list(map(int, input().split()))
for _ in range(r):
    u, v, c = map(int, input().split())
    G[u][v] = c
    G[v][u] = c

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if G[i][j] > G[i][k] + G[k][j]:
                G[i][j] = G[i][k] + G[k][j]

ans = -1
for i in range(1, n + 1):
    tmp = 0
    for j in range(1, n + 1):
        if G[i][j] <= m:
            tmp += items[j]
    ans = max(ans, tmp)
print(ans)
