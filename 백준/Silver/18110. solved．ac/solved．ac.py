def f(n):
    return int(n) + [1, 0][n - int(n) < 0.5]
n = int(input())
if n == 0:
    print(0)
    exit()
arr = sorted([int(input()) for _ in range(n)])
m = f(n * 0.15)
if m != 0:
    arr = arr[m:-m]
print(f(sum(arr) / (n - 2 * m)))