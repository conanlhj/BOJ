n = int(input())
arr = sorted(map(int, input().split()))
print(arr[2 * n - 1] - arr[n])
