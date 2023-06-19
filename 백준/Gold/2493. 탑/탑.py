s = []
r = []
input()
for i, a in enumerate(map(int, input().split())):
    while s and s[-1][1] <= a:
        s.pop()
    if s:
        r.append(s[-1][0])
    else:
        r.append(0)
    s.append((i + 1, a))
print(*r)