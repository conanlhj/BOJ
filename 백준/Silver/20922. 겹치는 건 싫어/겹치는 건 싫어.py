N, K = map(int, input().split())
a = list(map(int, input().split()))
b = [0] * 100001
front = 0
rear = 0
ans = 0
while front < N:
    if b[a[front]] == K:
        b[a[rear]] -= 1
        rear += 1
    else:
        b[a[front]] += 1
        front += 1
    ans = max(ans, front - rear)
print(ans)