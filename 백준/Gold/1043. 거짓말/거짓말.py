from collections import deque

N, M = map(int, input().split())
truth = list(map(int, input().split()))[1:]
party = [list(map(int, input().split()))[1:] for _ in range(M)]
know = [False] * (N + 1)
G = [[] for _ in range(N+1)]

for p in party:
    if len(p) == 1:
        G[p[0]].append(p[0])
    
    for i in range(len(p)-1):
        G[p[i]].append(p[i+1])
        G[p[i + 1]].append(p[i])

def bfs(start):
    q = deque([start])
    while q:
        u = q.popleft()
        for v in G[u]:
            if not know[v]:
                q.append(v)
                know[v] = True

for t in truth:
    if not know[t]:
        know[t] = True
        bfs(t)

result = 0
for p in party:
    flag = False
    for k in p:
        if know[k]:
            flag = True
            break
    if not flag:
        result += 1

print(result)