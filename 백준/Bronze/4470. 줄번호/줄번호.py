arr = []
for i in range(int(input())):
    arr.append(input())
for i in range(len(arr)):
    print(str(i + 1), end="")
    print(".", arr[i])