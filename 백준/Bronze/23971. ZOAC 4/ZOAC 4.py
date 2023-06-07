from math import ceil as c
H, W, N, M = map(int, input().split())
print(c(H / (N + 1)) * c(W / (M + 1)))