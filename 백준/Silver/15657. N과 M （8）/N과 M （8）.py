from itertools import combinations_with_replacement

N, M = map(int, input().split())
arr = sorted(map(int, input().split()))
for _ in combinations_with_replacement(arr, M):
    print(*_)