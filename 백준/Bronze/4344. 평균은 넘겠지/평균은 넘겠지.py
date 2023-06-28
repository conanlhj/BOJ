r = []
for i in range(int(input())):
    lst = list(map(int, input().split()))
    avg = sum(lst[1:]) / lst[0]
    cnt = 0
    for i in lst[1:]:
        if i > avg:
            cnt += 1
    res = 100 * cnt / lst[0]
    print("%.3f" % res + "%")