from itertools import combinations

N = int(input())
a = list(map(int, input().split()))
s = set()
for i in range(1, N):
    for c in combinations(a, i):
        s.add(sum(c))
print(sum(a) - len(s) - 1)