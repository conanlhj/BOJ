N, M = map(int, input().split())
nums = sorted(map(int, input().split()))
visited = [False] * N


def backtracking(arr):
    if len(arr) == M:
        print(*arr)

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            backtracking(arr + [nums[i]])
            visited[i] = False


backtracking([])
