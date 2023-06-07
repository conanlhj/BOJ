N = int(input())
a = list(map(int, input().split()))

increase = [False] * (N - 1)
decrease = [False] * (N - 1)

for i in range(N - 1):
    if a[i] <= a[i + 1]:
        increase[i] = True
    if a[i] >= a[i + 1]:
        decrease[i] = True

inc = increase.count(False)
dec = decrease.count(False)
if inc == 0 or dec == 0:
    print(0)
elif (inc == 1 and a[-1] <= a[0]) and (dec == 1 and a[-1] >= a[0]):
    print(min(increase.index(False), decrease.index(False)) + 1)
elif inc == 1 and a[-1] <= a[0]:
    print(increase.index(False) + 1)
elif dec == 1 and a[-1] >= a[0]:
    print(decrease.index(False) + 1)
else:
    print(-1)