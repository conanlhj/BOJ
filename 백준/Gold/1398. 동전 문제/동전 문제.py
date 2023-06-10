dp = [0] * 101
for i in range(1, 101):
    dp[i] = dp[i-1] + 1
    if i >= 10:
        dp[i] = min(dp[i], dp[i - 10] + 1)
    if i >= 25:
        dp[i] = min(dp[i], dp[i - 25] + 1)
for t in range(int(input())):
    C = input()
    if len(C) % 2:
        C = "0" + C
    res = 0
    for i in range(0, len(C), 2):
        tmp = int(C[i:i+2])
        res += dp[tmp]
    print(res)