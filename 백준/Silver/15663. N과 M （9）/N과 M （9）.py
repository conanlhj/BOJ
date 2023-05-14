from itertools import combinations

N, M = map(int, input().split())
arr = sorted(map(int, input().split()))
visited = [False] * N
result = [-1]

def bk(d):
    if d == M:
        print(*result[1:])
        return

    last_used = -1
    
    for i in range(N):
        if not visited[i] and arr[i] != last_used:
            result.append(arr[i])
            visited[i] = True
            last_used = arr[i]
            bk(d+1)
            result.pop()
            visited[i] = False

bk(0)