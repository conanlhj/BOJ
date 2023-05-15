N, B = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(N)]

def matxmat(A, B):
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result[i][j] = sum(A[i][k] * B[k][j] for k in range(N)) % 1000
    return result


def pow(A, b):
    if b == 1:
        for i in range(N):
            for j in range(N):
                A[i][j] %= 1000
        return A
    
    x = pow(A, b//2)
    if b % 2:
        return matxmat(matxmat(x, x), A)
    else:
        return matxmat(x, x)

result = pow(mat, B)
for _ in result:
    print(*_)