dp = [[0] * 3 for _ in range(100000)]
for i in range(3):
    for j in range(i + 1):
        dp[i][j] = 1
dp[1][0] = 0
for i in range(3, 100000):
    dp[i][0] = dp[i - 1][1] % 1000000009 + dp[i - 1][2] % 1000000009
    dp[i][1] = dp[i - 2][0] % 1000000009 + dp[i - 2][2] % 1000000009
    dp[i][2] = dp[i - 3][0] % 1000000009 + dp[i - 3][1] % 1000000009
for t in range(int(input())):
    print(sum(dp[int(input()) - 1]) % 1000000009)