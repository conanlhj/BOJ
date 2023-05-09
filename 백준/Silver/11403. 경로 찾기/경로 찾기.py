N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i != k and j != k and not A[i][j]:
                A[i][j] = A[i][k] & A[k][j]

for a in A:
    print(*a)
