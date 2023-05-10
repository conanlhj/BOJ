import sys

sys.setrecursionlimit(100001)
input = sys.stdin.readline
n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
preorder = []


def f(in_left, in_right, post_left, post_right):
    if in_right - in_left != post_right - post_left:
        return

    if in_left < in_right and post_left < post_right:
        for i in range(in_right - in_left):
            if inorder[in_left + i] == postorder[post_right - 1]:
                preorder.append(postorder[post_right - 1])
                f(in_left, in_left + i, post_left, post_left + i)
                f(in_left + i + 1, in_right, post_left + i, post_right - 1)


f(0, n, 0, n)
print(*preorder)
