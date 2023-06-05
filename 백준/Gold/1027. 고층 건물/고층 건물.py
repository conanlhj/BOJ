N = int(input())
h = list(map(int, input().split()))
see = [[True] * N for _ in range(N)]
for i in range(N - 1):
    for j in range(i + 1, N):
        a = (h[j] - h[i]) / (j - i)
        b = h[i]
        for k in range(i + 1, j):
            if h[k] >= a * (k - i) + b:
                see[i][j] = False
                see[j][i] = False
                break
print(max([sum(i) for i in see]) - 1)