N, K = map(int, input().split())
arr = []
for _ in range(N):
    P = int(input())
    tmp = list(map(int, input().split()))
    d = []
    for i in range(P):
        x, y = tmp[2 * i], tmp[2 * i + 1]
        d.append(x*x + y*y)
    arr.append(max(d))
arr.sort()
print("%.2f" % round(arr[K-1], 2))