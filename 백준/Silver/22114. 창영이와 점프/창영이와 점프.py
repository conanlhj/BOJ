N, K = map(int, input().split())
L = [0] + list(map(int, input().split()))
dp = [[1] * N for _ in range(2)]
for i in range(1, N):
  if L[i] <= K:
    dp[0][i] = dp[0][i-1] + 1
    dp[1][i] = dp[1][i-1] + 1
  else:
    dp[0][i] = 1
    dp[1][i] = max(dp[0][i-1] + 1, 1)

print(max(max(dp[0]), max(dp[1])))