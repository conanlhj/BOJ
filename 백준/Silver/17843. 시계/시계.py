for t in range(int(input())):
    h, m, s = map(int, input().split())
    t = 3600*h+60*m+s
    h, m, s = t/120%360, t/10%360, t*6%360
    arr = [h, m, s, h]
    ans = 1000
    for i in range(3):
        x, y = arr[i], arr[i+1]
        ang = abs(x - y)
        if ang > 180:
            ang = 360 - ang
        ans = min(ang, ans)
    print(ans)