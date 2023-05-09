from collections import deque
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    A, B = map(int, input().split())
    q = deque()
    q.append((A, ""))
    visit = [False] * 10000
    while q:
        ｎ, p = q.popleft()
        visit[n] = True
        if n == B:
            print(p)
            break
        d = (2 * n) % 10000
        if not visit[d]:
            q.append((d, p + "D"))
            visit[d] = True
        s = (n - 1) % 10000
        if not visit[s]:
            q.append((s, p + "S"))
            visit[s] = True
        l = (10 * n + (n // 1000)) % 10000
        if not visit[l]:
            q.append((l, p + "L"))
            visit[l] = True
        r = (n // 10 + (n % 10) * 1000) % 10000
        if not visit[r]:
            q.append((r, p + "R"))
            visit[r] = True