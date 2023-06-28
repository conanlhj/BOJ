X = 0
N = int(input())
A, B, C, D, E, F = map(int, input().split())
for a in range(1, N % F + 1):
    i = N // F * F + a
    if not i % A:
        X = X + i
    if not i % B:
        X = X % i
    if not i % C:
        X = X & i
    if not i % D:
        X = X ^ i
    if not i % E:
        X = X | i
    if not i % F:
        X = X >> i
print(X)