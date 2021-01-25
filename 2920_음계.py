i = list(map(int, input().split()))
asc = sorted(i)
if asc == i:
    print('ascending')
elif asc[::-1] == i:
    print('descending')
else:
    print('mixed')
