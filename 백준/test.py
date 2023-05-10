for t in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())), list(map(int, input().split()))]
    dp = [[0] * n, [0] * n]
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    for i in range(1, n):
        dp[0][i] = max(
            dp[1][i - 1] + arr[0][i],
            dp[0][i - 2] + arr[0][i] if i > 1 else -1,
            dp[1][i - 2] + arr[0][i] if i > 1 else -1,
        )
        dp[1][i] = max(
            dp[0][i - 1] + arr[1][i],
            dp[1][i - 2] + arr[1][i] if i > 1 else -1,
            dp[0][i - 2] + arr[1][i] if i > 1 else -1,
        )
    print(max(max(dp[0]), max(dp[1])))
