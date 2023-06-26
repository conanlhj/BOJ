N, K = map(int, input().split())
L = list(map(int, input().split()))
arr = [1]
for i in L:
    if i > K:
        arr.append(1)
    else:
        arr[-1] += 1
if len(arr) == 1:
    print(arr[0])
else:
    print(max([arr[i+1] + arr[i] for i in range(len(arr)-1)]))