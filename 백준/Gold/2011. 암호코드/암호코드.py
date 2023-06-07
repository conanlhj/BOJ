A = input()
if A[0] == '0':
    print(0)
else:
    dp = [0] * (len(A)+1)
    dp[0], dp[1] = 1, 1
    for i in range(2, len(A)+1):
        if A[i-1] != '0':
            dp[i] = dp[i-1]
        if 9 < int(A[i-2:i]) < 27:
            dp[i] += dp[i-2]
        dp[i] %= 1000000
    print(dp[-1])