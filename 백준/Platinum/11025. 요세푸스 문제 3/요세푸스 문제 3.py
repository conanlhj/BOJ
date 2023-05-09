n, k = map(int, input().split())
t, result = 1, 1
while t <= n:
    result = (result+k-1)%t+1
    t += 1
print(result)