from collections import deque


def dist(u, v):
    u = arr[u]
    v = arr[v]
    return abs(u[0] - v[0]) + abs(u[1] - v[1])


def bfs(s):
    q = deque([s])
    visited[s] = True
    while q:
        x = q.popleft()
        if x == n - 1:
            return True
        for y in edges[x]:
            if not visited[y]:
                visited[y] = True
                q.append(y)
    return False


for t in range(int(input())):
    n = int(input()) + 2
    arr = [tuple(map(int, input().split())) for _ in range(n)]
    visited = [False] * n
    edges = [[] for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if u != v and dist(u, v) <= 1000:
                edges[u].append(v)
    print(["sad", "happy"][bfs(0)])
