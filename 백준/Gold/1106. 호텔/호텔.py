C, N = map(int, input().split())
dp = [10000001] * (C + 100)
dp[0] = 0
arr = [tuple(map(int, input().split())) for _ in range(N)]

for cost, gain in arr:
    for i in range(gain, C + 100):
        dp[i] = min(dp[i], dp[i - gain] + cost)
print(min(dp[C:]))
