n, a, w = map(str, input().split())
while n != '#' and a != '0' and w != '0':
    if int(a) > 17 or int(w) >= 80:
        print(n, "Senior")
    else:
        print(n, "Junior")
    n, a, w = map(str, input().split())