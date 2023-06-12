dp = [1] * 50001
dp[1] = 2
dp[2] = 3
for i in range(3, 50001):
    dp[i] = sum(dp[i - 3 : i]) % 1000000009
for t in range(int(input())):
    print(dp[int(input()) // 2])