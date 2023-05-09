N, M = map(int, input().split())
arr = list(map(int, input().split()))
dp = [0] * (N + 1)
dp[1] = arr[0]
for i in range(2, N + 1):
    dp[i] = dp[i - 1] + arr[i - 1]

for i, j in [map(int, input().split()) for _ in range(M)]:
    print(dp[j] - dp[i - 1])
