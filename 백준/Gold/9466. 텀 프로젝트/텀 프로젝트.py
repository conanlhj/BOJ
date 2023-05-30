import sys
sys.setrecursionlimit(int(1e9))


def dfs(x):
    global cycleCnt
    visited[x] = True
    isCycle.append(x)

    next = arr[x]
    if visited[next] == True:
        if next in isCycle:
            cycleCnt += len(isCycle) - isCycle.index(next)
        return
    dfs(next)


for t in range(int(input())):
    n = int(input())
    arr = list(map(lambda x: int(x) - 1, input().split()))
    visited = [False] * n
    cycleCnt = 0
    for i in range(n):
        if not visited[i]:
            isCycle = []
            dfs(i)
    print(n - cycleCnt)
