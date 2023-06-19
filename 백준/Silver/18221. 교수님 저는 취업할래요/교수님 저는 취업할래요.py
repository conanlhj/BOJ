N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
a, b, c, d = [0]*4
stu = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 5:
            a, b = i, j
        elif arr[i][j] == 2:
            c, d = i, j
        elif arr[i][j] == 1:
            stu.append((i, j))
min_x, min_y = min(a, c), min(b, d)
max_x, max_y = max(a, c), max(b, d)
cnt = 0
for x, y in stu:
    if min_x <= x <= max_x and min_y <= y <= max_y:
        cnt += 1
if cnt >= 3 and (a-c)**2 + (b-d)**2 >= 25:
    print(1)
else:
    print(0)