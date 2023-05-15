import sys

INF = sys.maxsize

for t in range(int(input())):
    N, M, W = map(int, input().split())
    edges = []
    dis = [INF] * (N + 1)

    for _ in range(M):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
    for _ in range(W):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    dis[1] = 0
    flag = False
    for i in range(N):
        for u, v, c in edges:
            if dis[v] > c + dis[u]:
                dis[v] = c + dis[u]
                if i == N - 1:
                    flag = True
                    break
    if flag:
        print("YES")
    else:
        print("NO")
