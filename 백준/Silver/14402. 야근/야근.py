n = int(input())
d = {}
ans = 0
for _ in range(n):
    s, p = input().split()

    if p == "+":
        if s in d.keys():
            d[s] += 1
        else:
            d[s] = 1
    else:
        if s in d.keys():
            if d[s] == 0:
                ans += 1
            else:
                d[s] -= 1
        else:
            ans += 1

ans += sum(d.values())
print(ans)
