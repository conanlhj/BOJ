n, s, p = map(int, input().split())
if not n:
    print(1)
    exit()
arr = list(map(int, input().split()))
if n == p and arr[-1] >= s:
    print(-1)
    exit()
ans = n + 1
for i in range(n):
    if arr[i] <= s:
        ans = i + 1
        break
print(ans)