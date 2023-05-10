from collections import deque


def bfs(u):
    global K
    Q = deque()
    Q.append((u, 0))
    while Q:
        x, c = Q.popleft()
        if x == K:
            return c
        for nx in [x - 1, x + 1, 2 * x]:
            if 0 <= nx < 100001 and not v[nx]:
                v[nx] = True
                Q.append((nx, c + 1))


global K
N, K = map(int, input().split())
v = [False] * 100001
print(bfs(N))
