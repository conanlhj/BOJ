dp = [[0] * 3 for _ in range(10000)]
for i in range(3):
    for j in range(i + 1):
        dp[i][j] = 1
for i in range(3, 10000):
    for j in range(1, 4):
        dp[i][j - 1] = sum(dp[i - j][0:j])
for _ in range(int(input())):
    print(sum(dp[int(input()) - 1]))