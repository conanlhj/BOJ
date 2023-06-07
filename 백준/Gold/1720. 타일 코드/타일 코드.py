N = int(input())
dp = [0] * (N + 1)
dp[0] = 1
dp[1] = 1

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 2 * dp[i - 2]

if N % 2:
    print((dp[N] + dp[N // 2]) // 2)
else:
    print((dp[N] + dp[N // 2] + 2 * dp[N // 2 - 1]) // 2)
