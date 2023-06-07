hexa = [1, 6, 15, 28, 45, 66]
N = int(input())

for i in range(6, N + 1):
    num = i * (2 * i - 1)
    if num > N:
        break
    hexa.append(num)

dp = [0] * (N + 1)
dp[1] = 1

for i in range(2, N + 1):
    tmp = int(1e9)
    for h in hexa:
        if i - h >= 0:
            tmp = min(tmp, dp[i - h])
        else:
            break
    dp[i] = tmp + 1
print(dp[-1])
