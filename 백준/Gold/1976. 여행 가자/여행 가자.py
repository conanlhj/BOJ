from collections import deque

N = int(input())
M = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(lambda x: int(x) - 1, input().split()))
visited = [0] * N


def bfs(v, cnt):
    q = deque([v])
    visited[v] = cnt
    while q:
        nv = q.popleft()
        for i in range(N):
            if A[nv][i] and visited[i] == 0:
                visited[i] = cnt
                q.append(i)


cnt = 1
for i in range(N):
    if visited[i] == 0:
        bfs(i, cnt)
        cnt += 1
flag = True
for i in range(M - 1):
    if visited[plan[i]] != visited[plan[i + 1]]:
        flag = False
        break
print(["NO", "YES"][flag])
