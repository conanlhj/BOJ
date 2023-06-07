N = int(input())
adj = [list(map(lambda x: 1 if x == "Y" else int(1e9), input())) for _ in range(N)]
for i in range(N):
    adj[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            if adj[i][j] > adj[i][k] + adj[k][j]:
                adj[i][j] = adj[i][k] + adj[k][j]

ans = 0
for i in range(N):
    tmp = 0
    for j in range(N):
        if adj[i][j] in [1, 2]:
            tmp += 1
    ans = max(ans, tmp)
print(ans)
