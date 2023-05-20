S = input()
n = int(input())
A = [input() for _ in range(n)]

dp = [False] * (len(S) + 1)
dp[len(S)] = True

for i in range(len(S) - 1, -1, -1):
    for w in A:
        if S[i : i + len(w)] == w and dp[i + len(w)]:
            dp[i] = True
            break

print(int(dp[0]))
