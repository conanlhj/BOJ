k, n = map(int, input().split())
arr = [input() for _ in range(k)]
result = [i for i in arr]
arr.sort(key=lambda x: (-int(x), len(x)))
result += [arr[0]] * (n - k)

for i in range(len(result)):
    for j in range(len(result) - i - 1):
        if result[j] + result[j + 1] < result[j + 1] + result[j]:
            result[j], result[j + 1] = result[j + 1], result[j]
print("".join(result))
