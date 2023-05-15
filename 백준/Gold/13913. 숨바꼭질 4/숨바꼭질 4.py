from collections import deque

N, K = map(int, input().split())
prev = [-1] * 100001

q = deque([(N, 0)])
while q:
    x, c = q.popleft()
    if x == K:
        break
    for nx in [x-1, x+1, 2*x]:
        if 0 <= nx < 100001 and prev[nx] == -1:
            prev[nx] = x
            q.append((nx, c + 1))

print(c)
arr = []
i = K
while i != N:
    arr.append(i)
    i = prev[i]
arr.append(N)
print(*arr[::-1])