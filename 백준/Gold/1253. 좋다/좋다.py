N = int(input())
arr = sorted(map(int, input().split()))
ans = 0
for i, tar in enumerate(arr):
    st, ed = 0, N - 1
    while st < ed:
        mid = arr[st] + arr[ed]
        if mid == tar and st != i and ed != i:
            ans += 1
            break
        elif st == i:
            st += 1
        elif ed == i:
            ed -= 1
        elif mid < tar:
            st += 1
        else:
            ed -= 1
print(ans)