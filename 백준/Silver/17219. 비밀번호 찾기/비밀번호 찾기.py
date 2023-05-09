import sys
input = sys.stdin.readline
N, M = map(int, input().split())
d = {i: j for i, j in [input().split() for _ in range(N)]}
for i in range(M):
    print(d[input().strip()])
