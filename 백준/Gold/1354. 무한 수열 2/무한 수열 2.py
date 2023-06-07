d = {}
N, P, Q, X, Y = map(int, input().split())


def f(i):
    if i <= 0:
        return 1

    if i in d.keys():
        return d[i]
    d[i // P - X] = f(i // P - X)
    d[i // Q - Y] = f(i // Q - Y)
    return d[i // P - X] + d[i // Q - Y]


print(f(N))
