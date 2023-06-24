n = int(input())
arr = list(map(int, input().split()))
sum_ = sum(arr)
max_ = max(arr)
if 2 * max_ > sum_ + 1:
    print((sum_-max_)*2 + 1)
else:
    print(sum_)