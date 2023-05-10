import sys

input = sys.stdin.readline


def f(A, n, c):
    if n == 1:
        return A % c
    x = f(A, n // 2, c)
    if n % 2:
        return (x * x * A) % c
    return (x * x) % c


A, B, C = map(int, input().split())
print(f(A, B, C))
