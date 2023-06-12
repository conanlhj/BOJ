dp = [0] * 1000001
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, 1000001):
    dp[i] = sum(dp[i - j] for j in range(1, 4)) % 1000000009
for t in range(int(input())):
    print(dp[int(input())])