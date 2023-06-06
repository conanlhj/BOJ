import sys
from collections import deque
input = sys.stdin.readline
N, L = map(int,input().split())
A = list(map(int, input().split()))
q = deque([])
for i in range(N):
    if q and q[0][0] <= i - L:
        q.popleft()
    while len(q) >= 1 and A[i] < q[-1][1]:
        q.pop()
    q.append((i, A[i]))
    print(q[0][1], end=" ")