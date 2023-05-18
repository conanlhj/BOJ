N, P, Q = map(int, input().split())
A = {0: 1}


def dfs(n):
    if n in A.keys():
        return A[n]

    A[n] = dfs(n // P) + dfs(n // Q)
    return A[n]


print(dfs(N))
