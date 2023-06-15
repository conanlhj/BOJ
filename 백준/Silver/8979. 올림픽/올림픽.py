N, K = map(int, input().split())
arr = []
d = {}
for _ in range(N):
    n, *tmp = map(int, input().split())
    arr.append([tmp, n])
    d[n] = 0
arr.sort(reverse=True)
d[arr[0][1]] = 1
cnt = 2
for i in range(1, N):
    if arr[i][0] == arr[i-1][0]:
        d[arr[i][1]] = d[arr[i-1][1]]
    else:
        d[arr[i][1]] = cnt
    cnt += 1
print(d[K])