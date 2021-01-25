n, q = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(q):
    m, *a, x = map(int, input().split())
    if m == 1:
        for i in range(a[0]-1, a[1]):
            arr[i] = x
    elif m == 2:
        cnt = 1
        for i in range(a[0]-1, a[1]):
            arr[i] += (cnt)*x
            cnt += 1
    elif m == 3:
        arr.insert(a[0]-1, x)
    else:
        print((sum(arr[a[0]-1:x])))
