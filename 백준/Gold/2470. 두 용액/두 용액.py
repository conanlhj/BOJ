n = int(input())
arr = sorted(map(int, input().split()))
st, ed = 0, n-1
min_val = abs(arr[st] + arr[ed])
ans = [arr[st], arr[ed]]
while st < ed:
    tmp = arr[st] + arr[ed]
    if abs(tmp) < min_val:
        min_val = abs(tmp)
        ans = [arr[st], arr[ed]]
        if tmp == 0:
            break
    
    if tmp < 0:
        st += 1
    else:
        ed -= 1
    
print(*ans)