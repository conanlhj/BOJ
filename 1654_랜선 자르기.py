k, n = map(int, input().split())
lan = [int(input()) for i in range(k)]
s, e = 1, max(lan)

while s <= e:
    m = (s+e)//2
    line = 0
    for i in lan:
        line += i // m
    if line >= n:
        s = m + 1
    else:
        e = m - 1
print(e)
