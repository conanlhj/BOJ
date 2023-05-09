for t in range(int(input())):
    n = int(input())
    t = {}
    for _ in range(n):
        a, b = input().split()
        if b in t:
            t[b] += 1
        else:
            t[b] = 1
    ans = 1
    for _ in t.values():
        ans *= _ + 1
    print(ans - 1)
