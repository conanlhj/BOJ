import math
a, b = sorted(map(int, input().split()))
x, y = map(int, input().split())
x = abs(x)
if not 0 <= y < x:
    print("Unknwon Number")
    exit()
p = math.ceil((a - y) / x)
q = math.floor((b - y) / x)
if q - p == 0:
    print(p * x + y)
else:
    print("Unknwon Number")