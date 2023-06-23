n = int(input())
st = list(input())
d = [0, 0]
for i in range(n - 1, -1, -1):
    d[st[i] == "s"] += 1
    if d[0] == d[1]:
        ans = st[i:]
print("".join(ans))