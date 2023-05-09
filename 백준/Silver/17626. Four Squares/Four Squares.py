import sys

input = sys.stdin.readline
n = int(input())
dp = [50000] * (n + 1)
dp[0] = 1
dp[1] = 1

for i in range(2, n + 1):
    j = 1
    while j**2 <= i:
        if j**2 == i:
            dp[i] = 1
            break
        dp[i] = min(dp[i], dp[i - j**2] + 1)
        j += 1
print(dp[-1])
