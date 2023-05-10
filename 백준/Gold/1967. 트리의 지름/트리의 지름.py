import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

V = int(input())
edges = [[] for _ in range(V)]

for _ in range(V - 1):
    u, v, cost = map(int, input().split())
    edges[u - 1].append((v - 1, cost))
    edges[v - 1].append((u - 1, cost))

visited = [-1] * V
visited[0] = 0


def dfs(x, y):
    for next, cost in edges[x]:
        if visited[next] == -1:
            visited[next] = cost + y
            dfs(next, cost + y)


dfs(0, 0)
s = visited.index(max(visited))
visited = [-1] * V
visited[s] = 0
dfs(s, 0)
print(max(visited))
