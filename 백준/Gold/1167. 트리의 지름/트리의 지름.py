import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

V = int(input())
edges = [[] for _ in range(V)]

for _ in range(V):
    vertex, *edge = list(map(int, input().split()))
    for i in range(len(edge) // 2):
        edges[vertex - 1].append((edge[2 * i] - 1, edge[2 * i + 1]))

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
