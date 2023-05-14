import math

M = int(input())
X = 1000000007
ans = 0

def f(n, s):
    if s == 1:
        return n % X
    if s % 2:
        return n * f(n, s-1) % X
    else:
        tmp = f(n, s//2)
        return tmp * tmp % X

for _ in range(M):
    n, s = map(int, input().split())
    ans += s * f(n, X-2) % X
    
print(ans % X)