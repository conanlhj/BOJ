def bt(eq, n):
    global cnt, found
    if found:
        return
    if n == 0:
        cnt += 1
        if cnt == K:
            found = True
            print(eq)
    for i in range(1, 4):
        if n >= i:
            bt(eq + f"+{i}", n - i)
N, K = map(int, input().split())
cnt = 0
found = False
for i in range(1, 4):
    if N >= i:
        bt(f"{i}", N - i)
if not found:
    print(-1)