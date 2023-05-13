from itertools import combinations

N, M = map(int, input().split())
store = []
house = []
for i in range(N):
    for j, n in enumerate(list(map(int, input().split()))):
        if n == 1:
            house.append((i, j))
        elif n == 2:
            store.append((i, j))

min_dist = int(1e9)
for stay in combinations(store, M):
    c_dist = 0
    for xh, yh in house:
        h_dist = int(1e9)
        for xs, ys in stay:
            h_dist = min(h_dist, abs(xh-xs) + abs(yh-ys))
        c_dist += h_dist
    min_dist = min(min_dist, c_dist)

print(min_dist)