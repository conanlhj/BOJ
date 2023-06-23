n, k = map(int, input().split())
coins = list(set(int(input()) for _ in range(n)))
dp = [int(1e9)] * 10001
dp[0] = 0
for i in range(1, 10001):
    min_val = int(1e9)
    for coin in coins:
        if i - coin >= 0:
            min_val = min(min_val, dp[i - coin] + 1)
    if min_val != int(1e9):
        dp[i] = min_val
if dp[k] == int(1e9):
    print(-1)
else:
    print(dp[k])