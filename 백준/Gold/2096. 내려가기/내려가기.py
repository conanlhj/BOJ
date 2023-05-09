dp_min = [0] * 3
dp_max = [0] * 3
for i in range(int(input())):
    arr = list(map(int, input().split()))

    dp_max = [
        max(dp_max[0:-1]) + arr[0],
        max(dp_max) + arr[1],
        max(dp_max[1:]) + arr[2],
    ]
    dp_min = [
        min(dp_min[0:-1]) + arr[0],
        min(dp_min) + arr[1],
        min(dp_min[1:]) + arr[2],
    ]

print(max(dp_max), min(dp_min))
