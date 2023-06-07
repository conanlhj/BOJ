N, K = map(int, input().split())
A = list(map(int, input().split()))

if N >= K:
    print(1)
    exit()

start = 2
end = K
ans = int(1e9)
while start <= end:
    mid = (start + end) // 2
    s = mid * (mid + 1) // 2
    
    for i in range(N-1):
        d = min(mid, A[i+1] - A[i])
        s += mid * d - (d - 1) * d / 2
    
    if s >= K:
        end = mid - 1
    else:
        start = mid + 1
print(start)