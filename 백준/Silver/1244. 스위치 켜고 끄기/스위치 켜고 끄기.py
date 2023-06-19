n = int(input())
s = list(map(int, input().split()))
m = int(input())
for sex, p in [map(int, input().split()) for _ in range(m)]:
    if sex == 1:
        for i in range(p - 1, n, p):
            s[i] = int(not s[i])
    else:
        st = ed = p - 1
        s[st] = int(not s[st])
        while 0 <= st and ed < n and s[st] == s[ed]:
            s[st] = int(not s[st])
            s[ed] = int(not s[ed])
            st -= 1
            ed += 1
for i in range(0, n, 20):
    print(*s[i : min(i + 20, n)])