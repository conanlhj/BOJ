N = int(input())
dp = [0] * N
dp[0] = 2
for i in range(1, N):
    dp[i] = 3 * dp[i - 1]
print(dp[-1])