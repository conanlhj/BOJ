dp = [[0] * 1001 for _ in range(1001)]
for i in range(1, 4):
    for j in range(1, i + 1):
        dp[i][j] = 1
dp[3][2] = 2
for i in range(4, 1001):
    for j in range(2, i + 1):
        dp[i][j] = sum(dp[i - k][j - 1] for k in range(1, 4)) % 1000000009

for t in range(int(input())):
    n, m = map(int, input().split())
    print(dp[n][m])