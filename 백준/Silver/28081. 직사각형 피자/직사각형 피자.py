W, H, K = map(int, input().split())
N = int(input())
y = [0] + list(map(int, input().split())) + [H]
M = int(input())
x = [0] + list(map(int, input().split())) + [W]

dy = sorted([y[i+1]-y[i] for i in range(N+1)])
dx = [x[i+1]-x[i] for i in range(M+1)]

def bs(tar):
    start = 0
    end = N
    while start <= end:
        mid = (start + end) // 2
        if dy[mid] * tar <= K:
            start = mid + 1
        else:
            end = mid - 1
    return start

cnt = 0
for i in dx:
    cnt += bs(i)
print(cnt)