input()
A = sorted(map(int, input().split()))
input()
m = list(map(int, input().split()))
for i in m:
    start, end = 0, len(A)-1
    while start <= end:
        mid = (start+end)//2
        if A[mid] == i:
            break
        if A[mid] > i:
            end = mid - 1
        else:
            start = mid + 1
    if A[mid] == i:
        print(1)
    else:
        print(0)
