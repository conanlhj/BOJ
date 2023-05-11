N, K = map(int, input().split())
dp = [[0] * (K + 1) for _ in range(N + 1)]

for i, (w, v) in enumerate([tuple(map(int, input().split())) for _ in range(N)]):
    for j in range(1, K + 1):
        if j < w:
            dp[i + 1][j] = dp[i][j]
        else:
            dp[i + 1][j] = max(v + dp[i][j - w], dp[i][j])
print(dp[-1][-1])
