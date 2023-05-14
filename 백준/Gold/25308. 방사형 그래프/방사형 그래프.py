from itertools import permutations

arr = list(map(int, input().split()))
ans = 0
for case in permutations(arr):
    n = len(case)
    flag = False
    for i in range(n-1):
        if case[i] < (2**.5) * case[i-1] * case[i+1] / (case[i-1] + case[i+1]):
            flag = True
            break
    if case[-1] < (2**.5) * case[-2] * case[0] / (case[-2] + case[0]):
        flag = True
    if not flag:
        ans += 1
print(ans)