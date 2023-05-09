import sys

sys.setrecursionlimit(10**9)
arr = []
while True:
    try:
        arr.append(int(sys.stdin.readline()))
    except:
        break


def postorder(root, e):
    if root > e:
        return
    m = e + 1

    for i in range(root + 1, e + 1):
        if arr[root] < arr[i]:
            m = i
            break
    postorder(root + 1, m - 1)
    postorder(m, e)
    print(arr[root])


postorder(0, len(arr) - 1)
