N, M = map(int, input().split())
arr = list(range(1, N + 1))
for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    arr[a : b + 1] = reversed(arr[a : b + 1])
print(*arr)
