n = int(input())
h = [int(input()) for i in range(n)]

h.insert(0, 0)
h += [0]
check = [0]
S = 0

for i in range(1, n + 2):
    while check and h[check[-1]] > h[i]:
        c_h = check.pop()
        S = max(S, (i - 1 - check[-1]) * h[c_h])
    check.append(i)
print(S)