N, M = map(int, input().split())
arr = sorted(map(int, input().split()))
result = [-1]

def bk(d):
    if d == M:
        print(*result[1:])
        return

    last_used = -1
    
    for i in range(N):
        if arr[i] != last_used and arr[i] >= result[-1]:
            result.append(arr[i])
            last_used = arr[i]
            bk(d+1)
            result.pop()

bk(0)