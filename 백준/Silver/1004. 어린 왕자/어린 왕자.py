for t in range(int(input())):
    x1, y1, x2, y2 = list(map(int, input().split()))
    cnt = 0
    for i in range(int(input())):
        xr, yr, c = map(int, input().split())
        d1 = (x1-xr)**2+(y1-yr)**2-c**2
        d2 = (x2-xr)**2+(y2-yr)**2-c**2
        if  d1*d2 < 0:
            cnt += 1
    print(cnt)